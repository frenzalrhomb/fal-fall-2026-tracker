import copy
import datetime as dt
import unittest
from tracker import append_snapshot, cache_quality, growth_pair, jikan_record


class DataQualityTests(unittest.TestCase):
    def test_old_cached_response_is_rejected_for_growth(self):
        observed, flags = cache_quality({"Last-Modified": "Sat, 11 Jul 2026 18:00:45 GMT"}, "2026-09-14T09:13:24+00:00")
        self.assertIn("stale_cache_metadata", flags)
        self.assertTrue(observed.startswith("2026-07-11"))

    def test_unknown_cache_age_is_not_assumed_fresh(self):
        self.assertIn("unknown_source_age", cache_quality({}, "2026-09-14T09:13:24+00:00")[1])

    def test_missing_score_stays_missing_and_response_id_is_checked(self):
        row = jikan_record(53913, {"data": {"mal_id": 53913, "members": 87372}}, {})
        self.assertIsNone(row["metrics"]["score"])
        self.assertFalse(row["eligible_for_growth"])
        with self.assertRaises(ValueError):
            jikan_record(53913, {"data": {"mal_id": 999}}, {})

    def test_reimporting_same_capture_does_not_create_false_observation(self):
        state = {}
        r = {"mal_id": 1, "source": "test", "observed_at": "2026-09-14T00:00:00+00:00", "metrics": {"members": 100}}
        self.assertTrue(append_snapshot(state, r))
        r["retrieved_at"] = "2026-09-20T00:00:00+00:00"
        self.assertFalse(append_snapshot(state, r))
        self.assertEqual(len(state["snapshots"]), 1)

    def test_growth_uses_elapsed_time_and_matching_sources(self):
        before = {"mal_id": 1, "source": "test", "observed_at": "2026-09-14T00:00:00+00:00", "metrics": {"members": 1000}, "eligible_for_growth": True}
        after = copy.deepcopy(before)
        after.update(observed_at="2026-09-16T12:00:00+00:00", metrics={"members": 1250})
        self.assertEqual(growth_pair(before, after)["per_day"], 100)
        after["source"] = "other"
        self.assertIsNone(growth_pair(before, after))
        after["source"] = "test"
        after["eligible_for_growth"] = False
        self.assertIsNone(growth_pair(before, after))

    def test_zero_and_missing_are_distinct(self):
        state = {}
        append_snapshot(state, {"mal_id": 1, "source": "test", "metrics": {"score": None, "dropped": 0}})
        self.assertIsNone(state["snapshots"][0]["metrics"]["score"])
        self.assertEqual(state["snapshots"][0]["metrics"]["dropped"], 0)


if __name__ == "__main__":
    unittest.main()
