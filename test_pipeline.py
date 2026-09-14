import copy
import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch
from urllib.error import HTTPError
import tracker
import external_collect as external
from reporting import momentum, build_report


def observation(day, members, source="mal_official", mid=1):
    return {"mal_id":mid,"source":source,"observed_at":f"2026-09-{day:02d}T12:00:00+00:00",
            "eligible_for_growth":True,"metrics":{"members":members}}


class PipelineTests(unittest.TestCase):
    def test_partial_collection_is_failure_even_with_successful_requests(self):
        self.assertFalse(tracker.collection_complete({"expected":69,"attempted":3,"successes":2,"errors":[{}]}))
        self.assertFalse(tracker.collection_complete({"expected":69,"attempted":69,"successes":68,"errors":[]}))
        self.assertTrue(tracker.collection_complete({"expected":69,"attempted":69,"successes":69,"errors":[]}))

    def test_auth_failure_stops_mal_and_preserves_run(self):
        state={"roster":[{"mal_id":1},{"mal_id":2}],"snapshots":[]}
        with patch.dict("os.environ",{"MAL_CLIENT_ID":"test-placeholder"}), patch.object(tracker,"save"), patch.object(tracker,"fetch",side_effect=HTTPError("test",401,"unauthorized",{},None)) as fetch:
            r=tracker.collect(state,"mal")
        self.assertEqual(fetch.call_count,1)
        self.assertFalse(tracker.collection_complete(r))
        self.assertEqual(state["runs"][-1]["stopped_reason"],"access_or_rate_limit")

    def test_daily_growth_does_not_mix_sources_or_count_reruns_as_days(self):
        records=[observation(14,1000),observation(15,1100),observation(16,1200),observation(16,9000,"other")]
        rerun=observation(15,1100)
        rerun["observed_at"]="2026-09-15T13:00:00+00:00"
        records.append(rerun)
        growth=momentum(records)
        self.assertEqual(growth["observed_days"],3)
        self.assertAlmostEqual(growth["per_day"],100,delta=1)
        self.assertIsNone(growth["pace_change"])

    def test_acceleration_needs_two_disjoint_supported_windows(self):
        records=[observation(d,1000+100*(d-14)) for d in range(14,18)]
        records += [observation(d,1500+200*(d-18)) for d in range(18,21)]
        m=momentum(records)
        self.assertIsNotNone(m["pace_change"])
        self.assertGreater(m["pace_change"],0)

    def test_single_day_and_stale_series_do_not_claim_recent_growth(self):
        self.assertIsNone(momentum([observation(14,1000)])["per_day"])
        # Wide gap: older observation falls outside recent window.
        self.assertIsNone(momentum([observation(14,1000),observation(20,2000)])["per_day"])

    def test_report_exposes_latest_counts_and_distinguishes_missing_score(self):
        r=observation(14,1100)
        r["metrics"].update(watching=3,completed=2,plan_to_watch=1095,dropped=0,on_hold=0,score=None,scored_by=0)
        r.update(airing_status="not_yet_aired",start_date="2026-10-04")
        state={"roster":[{"mal_id":1,"title":"Example","restricted":True,"premiere_date_jst":"2026-10-04"}],
               "snapshots":[r],"runs":[]}
        report,rows=build_report(state,generated_at="2026-09-14T13:00:00+00:00")
        self.assertIn("1,100",report)
        self.assertEqual(rows[0]["watching_completed"],5)
        self.assertEqual(rows[0]["dropped"],0)
        self.assertIsNone(rows[0]["score"])
        self.assertEqual(rows[0]["age_hours"],1)

    def test_anilist_matches_id_and_keeps_score_scale_separate(self):
        p={"data":{"Media":{"id":2,"idMal":1,"popularity":100,"favourites":3,"averageScore":85}}}
        r=external.anilist_record(1,p)
        self.assertEqual(r["metrics"]["average_score_100"],85)
        self.assertNotIn("score",r["metrics"])
        with self.assertRaises(ValueError):
            external.anilist_record(999,p)
        with self.assertRaises(ValueError):
            external.anilist_record(1,{"errors":[{"message":"bad field"}]})

    def test_anilist_access_denial_pauses_and_does_not_retry_other_titles(self):
        data={"snapshots":[],"runs":[]}
        with patch.object(external,"save"),patch.object(external,"request",side_effect=HTTPError("test",403,"forbidden",{},None)) as request:
            r=external.run_source("anilist",[{"mal_id":1},{"mal_id":2}],data)
            paused=external.run_source("anilist",[{"mal_id":1}],data)
        self.assertEqual(request.call_count,1)
        self.assertEqual(r["stopped_reason"],"access_denied_source_paused")
        self.assertEqual(paused["stopped_reason"],"paused_after_access_denial")

    def test_anilist_missing_ids_do_not_skip_later_titles(self):
        missing=HTTPError("test",404,"not found",{},None)
        payload={"data":{"Media":{"id":20,"idMal":4,"popularity":100,"favourites":0}}}
        data={"snapshots":[],"runs":[]}
        with patch.object(external,"save"),patch.object(external.time,"sleep"),patch.object(external,"request",side_effect=[missing,missing,missing,payload]) as request:
            r=external.run_source("anilist",[{"mal_id":i} for i in range(1,5)],data)
        self.assertEqual(request.call_count,4)
        self.assertEqual(r["missing_ids"],[1,2,3])
        self.assertEqual(len(r["errors"]),3)
        self.assertEqual(r["successes"],1)
        self.assertNotIn("stopped_reason",r)
        self.assertEqual(data["snapshots"][0]["mal_id"],4)

    def test_title_matching_requires_word_boundaries(self):
        self.assertEqual(external.title_matches("Psyren official trailer",["Psyren"]),["Psyren"])
        self.assertEqual(external.title_matches("Psyrenish unrelated post",["Psyren"]),[])
        self.assertEqual(external.title_matches("A new announcement",["A"]),[])

    def test_missing_youtube_key_does_not_claim_collection(self):
        with patch.dict("os.environ",{},clear=True),patch.object(external,"save"),patch.object(external,"request") as request:
            r=external.run_source("youtube",[],{"snapshots":[],"runs":[]})
        request.assert_not_called()
        self.assertEqual(r["successes"],0)
        self.assertEqual(r["stopped_reason"],"not_configured_YOUTUBE_API_KEY")


if __name__=="__main__":
    unittest.main()
