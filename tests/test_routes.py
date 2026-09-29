"""Placeholder: tests for route responses (expand in later phases)."""

import unittest

from app import app


class RouteSmokeTests(unittest.TestCase):
    """Smoke tests: each implemented route renders successfully."""

    def setUp(self):
        self.client = app.test_client()

    def test_dashboard_root(self):
        self.assertEqual(self.client.get("/").status_code, 200)

    def test_dashboard_alias(self):
        self.assertEqual(self.client.get("/dashboard").status_code, 200)

    def test_candidates(self):
        self.assertEqual(self.client.get("/candidates").status_code, 200)

    def test_candidate_detail(self):
        self.assertEqual(self.client.get("/candidates/WB-1001").status_code, 200)

    def test_candidate_detail_unknown_404(self):
        self.assertEqual(self.client.get("/candidates/NOPE").status_code, 404)

    def test_unbuilt_pages_404(self):
        """Calendar/interviews/jobs/activity routes do not exist yet."""
        for path in ("/calendar", "/interviews", "/jobs", "/activity"):
            self.assertEqual(self.client.get(path).status_code, 404, path)


if __name__ == "__main__":
    unittest.main()
