import unittest

from scripts.password_check import assess_password, has_obvious_pattern


class PasswordCheckTests(unittest.TestCase):
    def test_empty_input_is_not_safe_or_strong(self):
        self.assertEqual(assess_password("")["score"], 0)

    def test_common_password_example_is_weak(self):
        self.assertEqual(assess_password("password123")["score"], 0)

    def test_longer_candidate_scores_higher_than_short_candidate(self):
        short = assess_password("ab12")
        longer = assess_password("violet-cabin-moon-forest-93!")
        self.assertGreater(longer["score"], short["score"])

    def test_obvious_sequences_and_repetition_are_flagged(self):
        self.assertTrue(has_obvious_pattern("myabcdephrase"))
        self.assertTrue(has_obvious_pattern("ZZZZ-safe-example"))
        self.assertFalse(has_obvious_pattern("violet-cabin-moon"))

    def test_assessment_does_not_return_candidate(self):
        candidate = "fictional-long-candidate-482!"
        result = assess_password(candidate)
        self.assertNotIn(candidate, repr(result))

    def test_pattern_penalty_makes_result_more_conservative(self):
        regular = assess_password("violet-cabin-moon-forest-93!")
        patterned = assess_password("violet-cabin-moon-forest-abcde!")
        self.assertLessEqual(patterned["score"], regular["score"])


if __name__ == "__main__":
    unittest.main()
