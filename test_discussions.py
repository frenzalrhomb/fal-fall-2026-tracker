import datetime as dt
import unittest
from unittest.mock import patch
from discussions import (episode_number, minimal_post, week_counts, read_topic,
                         discover, latest_discussion, paginated, Client)
import urllib.error
from fal_points import cutoff, score_row, weekly_rows
from reporting import build_report

UTC = dt.timezone.utc


def post(pid, user, when):
    return {'id': pid, 'created_by': {'id': user, 'name': 'irrelevant'}, 'created_at': when,
            'body': 'Never store this', 'signature': 'Never store this either'}


def thread(tid, ep, posts):
    return {'topic_id': tid, 'title': f'A Season 3 Episode {ep} Discussion', 'episode': ep,
            'posts': [minimal_post(p) for p in posts], 'complete': True}


class FakeClient:
    def __init__(self, payloads):
        self.payloads = iter(payloads)
        self.urls = []

    def get(self, url):
        self.urls.append(url)
        item = next(self.payloads)
        if isinstance(item, Exception):
            raise item
        return item, {}


class DiscussionTests(unittest.TestCase):
    def test_unavailable_jikan_is_not_retried_for_every_title(self):
        client = Client('test-only', interval=0)
        with patch('discussions.urllib.request.urlopen', side_effect=urllib.error.URLError('DNS unavailable')) as request:
            for mid in (1, 2, 3):
                with self.assertRaises(urllib.error.URLError):
                    client.get(f'https://api.jikan.moe/v4/anime/{mid}/forum?filter=episode')
            self.assertEqual(request.call_count, 1)
            with self.assertRaises(urllib.error.URLError):
                client.get('https://api.myanimelist.net/v2/forum/topics?q=A')
            self.assertEqual(request.call_count, 2)

    def test_per_thread_dedup_and_week2_all_posts(self):
        ts = [thread(1, 1, [post(1, 7, '2026-09-01T12:00:00Z'), post(2, 7, '2026-10-10T12:00:00Z')]),
              thread(2, 2, [post(3, 7, '2026-10-11T12:00:00Z'), post(4, 8, '2026-10-11T22:01:00Z')])]
        counts = week_counts(ts, 2, cutoff(2)+dt.timedelta(hours=1))
        self.assertEqual(counts['participants'], 2)
        self.assertEqual(counts['window_end'], cutoff(2).isoformat())
        self.assertIsNone(counts['window_start'])

    def test_window_edges_and_week13(self):
        start = cutoff(4)-dt.timedelta(weeks=2)
        ts = [thread(1, 1, [post(1, 1, start.isoformat()), post(2, 2, (start+dt.timedelta(seconds=1)).isoformat()),
                           post(3, 3, cutoff(4).isoformat()), post(4, 4, (cutoff(4)+dt.timedelta(seconds=1)).isoformat())])]
        self.assertEqual(week_counts(ts, 4, cutoff(4)+dt.timedelta(days=1))['participants'], 2)
        self.assertEqual(week_counts(ts, 13, cutoff(13))['window_start'], (cutoff(13)-dt.timedelta(weeks=1)).isoformat())

    def test_exact_title_rejects_wrong_sequel_and_non_episode(self):
        self.assertEqual(episode_number('A Season 3 Episode 2 Discussion', ['A Season 3']), 2)
        self.assertIsNone(episode_number('A Season 2 Episode 2 Discussion', ['A Season 3']))
        self.assertIsNone(episode_number('A Season 3 trailer discussion', ['A Season 3']))

    def test_metadata_discards_body_and_requires_author(self):
        stored = minimal_post(post(1, 7, '2026-10-10T12:00:00Z'))
        self.assertEqual(set(stored), {'post_id', 'created_at', 'author_key'})
        self.assertNotIn('irrelevant', str(stored))
        with self.assertRaises(ValueError):
            minimal_post({'id': 2, 'created_at': '2026-10-10T12:00:00Z'})

    def test_topic_pagination_duplicate_posts_and_poll_ignored(self):
        title = 'A Season 3 Episode 1 Discussion'
        p = post(1, 7, '2026-10-10T12:00:00Z')
        client = FakeClient([
            {'data': {'title': title, 'posts': [p], 'poll': {'votes': 999}},
             'paging': {'next': 'https://api.myanimelist.net/v2/forum/topic/1?offset=100'}},
            {'data': {'title': title, 'posts': [p, post(2, 7, '2026-10-10T13:00:00Z')]}, 'paging': {}}])
        result = read_topic(client, {'topic_id': 1, 'title': title, 'episode': 1})
        self.assertTrue(result['complete'])
        self.assertEqual(len(result['posts']), 2)
        self.assertEqual(week_counts([result], 2, cutoff(2))['participants'], 1)
        self.assertEqual(len(client.urls), 2)

    def test_failed_page_remains_partial(self):
        title = 'A Season 3 Episode 1 Discussion'
        client = FakeClient([{'data': {'title': title, 'posts': [post(1, 7, '2026-10-10T12:00:00Z')]},
                              'paging': {'next': 'https://api.myanimelist.net/v2/forum/topic/1?offset=100'}}, TimeoutError()])
        result = read_topic(client, {'topic_id': 1, 'title': title, 'episode': 1})
        self.assertFalse(result['complete'])
        self.assertEqual(len(result['posts']), 1)

    def test_search_finds_aristocrat_without_episode_list(self):
        anime = {'mal_id': 60601, 'title': 'Tensei Kizoku, Kantei Skill de Nariagaru 3rd Season'}
        title = anime['title']+' Episode 1 Discussion'
        client = FakeClient([{'data': []}, {'data': [{'id': 9, 'title': title},
                             {'id': 10, 'title': 'Tensei Kizoku, Kantei Skill de Nariagaru 2nd Season Episode 1 Discussion'}]}])
        topics, ok, errors, flags = discover(client, anime, 'Aristocrat 3', {'search_query': 'Tensei Kizoku'}, [])
        self.assertTrue(ok)
        self.assertEqual([t['topic_id'] for t in topics], [9])
        self.assertIn('forum/topics?', client.urls[1])

    def test_empty_search_is_unknown_not_zero(self):
        client = FakeClient([{'data': []}, {'data': []}])
        _, ok, _, flags = discover(client, {'mal_id': 1, 'title': 'A'}, 'A', {}, [])
        self.assertFalse(ok)
        self.assertIn('no_episode_threads_found_not_proof_of_zero', flags)

    def test_repeated_search_pagination_rejected(self):
        url = 'https://api.myanimelist.net/v2/forum/topics?q=A'
        with self.assertRaises(ValueError):
            paginated(FakeClient([{'data': [], 'paging': {'next': url}}]), url, lambda p:p['data'])

    def test_report_points_partial_unknown_and_stale(self):
        moment = cutoff(2)-dt.timedelta(hours=1)
        anime = {'mal_id': 60601, 'title': 'A', 'restricted': False, 'premiere_date_jst': '2026-10-01'}
        official = {'mal_id': 60601, 'source': 'mal_official', 'observed_at': moment.isoformat(),
                    'airing_status': 'currently_airing', 'metrics': {'watching': 1000, 'completed': 20}}
        d = {'mal_id': 60601, 'observed_at': moment.isoformat(), 'usable': True, 'weeks': {'2': {
             'participants': 10, 'threads': [{'topic_id': 9, 'episode': 1, 'participants': 10, 'posts_complete': True}]}}}
        r = score_row(anime, official, None, 2, d)
        self.assertEqual(r['points']['total'], 765+750)
        report, _ = build_report({'roster': [anime], 'snapshots': [official]}, generated_at=moment.isoformat(),
                                 discussion_state={'snapshots': [d]})
        self.assertIn('topicid=9', report)
        self.assertIn('Your roster', report)
        self.assertIn('1,515', report)
        d['usable'] = False
        self.assertIsNone(score_row(anime, official, None, 2, d)['points']['total'])
        self.assertIsNone(latest_discussion({'snapshots': [d]}, 60601, 2, moment+dt.timedelta(hours=37)))

    def test_archive_preserves_pre_and_post_cutoff_observations(self):
        a = {'mal_id': 1, 'observed_at': (cutoff(2)-dt.timedelta(minutes=30)).isoformat(), 'weeks': {'2': {}}}
        b = {'mal_id': 1, 'observed_at': (cutoff(2)+dt.timedelta(minutes=15)).isoformat(), 'weeks': {'2': {}}}
        self.assertIs(latest_discussion({'snapshots': [a,b]}, 1, 2, cutoff(2)+dt.timedelta(hours=1), archived=True), b)

    def test_unlinked_forum_search_does_not_become_confirmed_fal_points(self):
        moment = cutoff(2)-dt.timedelta(hours=1)
        t = thread(1, 1, [post(1, 1, moment.isoformat())])
        w = week_counts([t], 2, moment)
        self.assertEqual(w['unlinked_participants'], 1)
        d = {'usable': True, 'weeks': {'2': w}}
        r = score_row({'mal_id': 1}, {'metrics': {'watching': 100, 'completed': 0}, 'airing_status': 'currently_airing'}, None, 2, d)
        self.assertIsNone(r['points']['total'])
        t['discovered_by'] = 'anime_forum_link'
        d['weeks']['2'] = week_counts([t], 2, moment)
        self.assertEqual(score_row({'mal_id': 1}, {'metrics': {'watching': 100, 'completed': 0}, 'airing_status': 'currently_airing'}, None, 2, d)['points']['total'], 150)

    def test_full_field_shows_conditional_estimate_for_non_roster_title(self):
        moment = cutoff(2)-dt.timedelta(hours=1)
        anime = {'mal_id': 1, 'title': 'Outside roster', 'restricted': False, 'premiere_date_jst': '2026-10-01'}
        official = {'mal_id': 1, 'source': 'mal_official', 'observed_at': moment.isoformat(),
                    'airing_status': 'currently_airing', 'metrics': {'watching': 100, 'completed': 0}}
        d = {'mal_id': 1, 'observed_at': moment.isoformat(), 'usable': True,
             'weeks': {'2': {'participants': 2, 'unlinked_participants': 2, 'threads': []}}}
        report,_ = build_report({'roster': [anime], 'snapshots': [official]}, generated_at=moment.isoformat(), discussion_state={'snapshots': [d]})
        self.assertIn('Discussion-inclusive estimate', report)
        self.assertIn('| 75 | 225.00 | discussions |', report)


if __name__ == '__main__':
    unittest.main()
