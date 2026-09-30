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
        self.assertEqual(self.client.get("/candidates/WB0001").status_code, 200)

    def test_candidate_detail_unknown_404(self):
        self.assertEqual(self.client.get("/candidates/NOPE").status_code, 404)

    def test_calendar(self):
        self.assertEqual(self.client.get("/calendar").status_code, 200)

    def test_calendar_month_param(self):
        self.assertEqual(
            self.client.get("/calendar?month=2026-10").status_code, 200
        )

    def test_calendar_invalid_month_falls_back(self):
        self.assertEqual(
            self.client.get("/calendar?month=not-a-month").status_code, 200
        )

    def test_interviews(self):
        self.assertEqual(self.client.get("/interviews").status_code, 200)

    def test_jobs(self):
        self.assertEqual(self.client.get("/jobs").status_code, 200)

    def test_activity(self):
        self.assertEqual(self.client.get("/activity").status_code, 200)

    def test_styleguide(self):
        self.assertEqual(self.client.get("/styleguide").status_code, 200)


if __name__ == "__main__":
    unittest.main()
