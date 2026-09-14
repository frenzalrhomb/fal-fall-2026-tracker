import unittest
from scoring import weekly_components


class ScoringTests(unittest.TestCase):
    def test_premiere_and_missing_inputs(self):
        r=weekly_components(1,{},aired=False,bonus_mode="replacement")
        self.assertEqual(r["total"],0)
        self.assertIsNone(weekly_components(1,{},aired=True,bonus_mode="replacement")["total"])
        r=weekly_components(3,{"watching":10,"completed":0},aired=True,bonus_mode="replacement")
        self.assertIsNone(r["score"])
        self.assertIsNone(r["total"])

    def test_explicit_week13_bonus_interpretations(self):
        m={"watching":1000,"completed":200,"score":8,"dropped":10,"favorites":20,"episode_participants":30}
        replacement=weekly_components(13,m,aired=True,bonus_mode="replacement")
        additive=weekly_components(13,m,aired=True,bonus_mode="additive")
        self.assertEqual(replacement["total"],600+4500+70000-80+600)
        self.assertEqual(additive["total"],600+6750+105000-120+900)

    def test_even_week_and_negative_rating_points(self):
        m={"watching":1000,"completed":0,"episode_participants":0,"score":5.5}
        self.assertEqual(weekly_components(2,m,aired=True,bonus_mode="additive")["audience"],750)
        self.assertEqual(weekly_components(2,m,aired=True,bonus_mode="replacement")["audience"],250)
        self.assertEqual(weekly_components(3,m,aired=True,bonus_mode="replacement")["score"],-8750)

    def test_requires_valid_rule_mode(self):
        with self.assertRaises(ValueError):
            weekly_components(13,{},aired=True,bonus_mode="unknown")


if __name__=="__main__":
    unittest.main()
