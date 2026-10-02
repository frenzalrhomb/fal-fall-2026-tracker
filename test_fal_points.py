import datetime as dt
import unittest
from fal_points import cutoff, current_week, nearest_cutoff, score_row, weekly_rows
from scoring import weekly_components
from reporting import build_report

UTC = dt.timezone.utc


class WeekPointsTests(unittest.TestCase):
    def test_calendar_and_mixed_bonus_rules(self):
        self.assertEqual(cutoff(1).isoformat(), "2026-10-04T22:00:00+00:00")
        self.assertEqual(cutoff(13).isoformat(), "2026-12-27T22:00:00+00:00")
        self.assertEqual(current_week(cutoff(1)-dt.timedelta(seconds=1)), 1)
        self.assertEqual(current_week(cutoff(1)), 2)
        m = {"watching": 1000, "completed": 200, "score": 8,
             "dropped": 10, "favorites": 20, "episode_participants": 30}
        self.assertEqual(weekly_components(2, m, aired=True, bonus_mode="fal_2026")["audience"], 900)
        self.assertEqual(weekly_components(3, m, aired=True, bonus_mode="fal_2026")["score"], 35000)
        self.assertEqual(weekly_components(4, m, aired=True, bonus_mode="fal_2026")["dropped"], -40)
        self.assertEqual(weekly_components(5, m, aired=True, bonus_mode="fal_2026")["favorites"], 300)
        w13 = weekly_components(13, m, aired=True, bonus_mode="fal_2026")
        self.assertEqual(w13["total"], 600+4500+70000-80+600)
        self.assertEqual(w13["known_subtotal"], w13["total"])

    def test_unknowns_and_pre_air(self):
        anime = {"mal_id": 1, "title": "A", "restricted": False, "premiere_date_jst": "2026-10-05"}
        snap = {"mal_id": 1, "source": "mal_official", "observed_at": "2026-10-04T21:00:00+00:00",
                "airing_status": "not_yet_aired",
                "metrics": {"watching": 50, "completed": 1, "dropped": 0, "score": None}}
        row = score_row(anime, snap, None, 1)
        self.assertEqual(row["points"]["audience"], 0)
        row = score_row(anime, snap, None, 13)
        self.assertEqual(row["points"]["known_subtotal"], -0)
        self.assertIn("favorites", row["points"]["missing"])
        self.assertIn("discussions", row["points"]["missing"])

    def test_archive_uses_near_cutoff_and_keeps_missing(self):
        anime = {"mal_id": 1, "title": "A", "restricted": False, "premiere_date_jst": "2026-10-01"}
        def snap(when, wc):
            return {"mal_id": 1, "source": "mal_official", "observed_at": when,
                    "airing_status": "currently_airing", "metrics": {
                        "watching": wc, "completed": 0, "score": 7.0, "dropped": 0}}
        before = snap("2026-10-04T20:17:00+00:00", 100)
        after = snap("2026-10-04T22:08:00+00:00", 110)
        state = {"roster": [anime], "snapshots": [before, after]}
        self.assertIs(nearest_cutoff(state["snapshots"], cutoff(1)), after)
        self.assertEqual(weekly_rows(state, 1, cutoff(1)+dt.timedelta(hours=1), archived=True)[0]["points"]["known_subtotal"], 55)
        report, _ = build_report(state, generated_at="2026-10-04T23:00:00+00:00")
        self.assertIn("English:", report)
        self.assertIn("/anime/1/_/stats", report)
        self.assertIn("Week 1", report)
        self.assertIn("+8 min", report)


if __name__ == "__main__":
    unittest.main()
