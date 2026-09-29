"""Placeholder: tests for candidate data and page behaviour (expand later)."""

import unittest

from mock import candidates


class CandidateMockDataTests(unittest.TestCase):
    """Minimal checks on the mock candidate dataset."""

    def test_candidates_exist(self):
        self.assertGreater(len(candidates.CANDIDATES), 0)

    def test_get_candidate(self):
        self.assertIsNotNone(candidates.get_candidate("WB-1001"))
        self.assertIsNone(candidates.get_candidate("NOPE"))


if __name__ == "__main__":
    unittest.main()
