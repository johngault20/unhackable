import unittest

from scripts.password_check import assess_password, has_obvious_pattern


class PasswordAssessmentTests(unittest.TestCase):
    def test_empty_input_is_not_scored_as_safe(self):
        result = assess_password("")
        self.assertEqual(result["score"], 0)
        self.assertIn("Enter a new candidate", result["label"])

    def test_common_and_substituted_fragments_score_zero(self):
        self.assertEqual(assess_password("password")["score"], 0)
        self.assertEqual(assess_password("P@ssw0rd123!")["score"], 0)

    def test_long_unpatterned_candidate_scores_higher_than_short_candidate(self):
        short = assess_password("ab12")
        longer = assess_password("River-candle-orbit-window-72")
        self.assertGreater(longer["score"], short["score"])

    def test_sequence_and_repetition_penalties(self):
        self.assertTrue(has_obvious_pattern("my-a-b-c-d-phrase"))
        self.assertTrue(has_obvious_pattern("abcdabcdabcd"))
        self.assertTrue(has_obvious_pattern("candidate-ending-2025"))
        self.assertFalse(has_obvious_pattern("violet-cabin-moon"))

    def test_result_does_not_echo_candidate(self):
        candidate = "A fictional candidate phrase 93!"
        result = assess_password(candidate)
        self.assertNotIn(candidate, repr(result))

    def test_score_is_bounded_and_no_crack_time_is_claimed(self):
        result = assess_password("violet-cabin-moon-river-cloud-amber")
        self.assertGreaterEqual(result["score"], 0)
        self.assertLessEqual(result["score"], 5)
        self.assertIn("cannot check", result["advice"])
        self.assertNotIn("seconds", result["advice"])


if __name__ == "__main__":
    unittest.main()
