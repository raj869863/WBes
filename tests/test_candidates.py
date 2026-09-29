"""Placeholder: tests for candidate data and page behaviour (expand later)."""

import unittest

from mock import candidates


class CandidateMockDataTests(unittest.TestCase):
    """Minimal checks on the mock candidate dataset."""

    def test_dataset_size(self):
        """The Candidates page spec expects 24 mock candidates."""
        self.assertEqual(len(candidates.CANDIDATES), 24)

    def test_candidates_exist(self):
        self.assertGreater(len(candidates.CANDIDATES), 0)

    def test_get_candidate(self):
        self.assertIsNotNone(candidates.get_candidate("WB0001"))
        self.assertIsNone(candidates.get_candidate("NOPE"))


if __name__ == "__main__":
    unittest.main()
