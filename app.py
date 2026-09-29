"""Wissen Baum Engineering Solutions - Internal HR Dashboard.

Phase 0: minimal Flask foundation.
Phase 1A: UI design system (+ /styleguide reference page).
Phase 2: Dashboard page (UI only, mock data - no external services yet).
Phase 3: Candidates page (UI only, mock data - search/filter/CSV, no backend).
"""

from flask import Flask, abort, render_template

import mock_candidates
import mock_data

app = Flask(__name__)


@app.route("/")
def dashboard():
    """Dashboard - recruitment & interview operations overview (mock data)."""
    return render_template(
        "dashboard.html",
        company=mock_data.COMPANY_NAME,
        kpis=mock_data.KPI_CARDS,
        statuses=mock_data.CANDIDATE_STATUSES,
        upcoming=mock_data.UPCOMING_INTERVIEWS,
        activity=mock_data.RECENT_ACTIVITY,
    )


@app.route("/candidates")
def candidates():
    """Candidates - searchable, filterable HR data table (mock data)."""
    return render_template(
        "candidates.html",
        company=mock_data.COMPANY_NAME,
        candidates=mock_candidates.CANDIDATES,
        filters=mock_candidates.filter_options(),
    )


@app.route("/candidates/<cid>")
def candidate_detail(cid):
    """Minimal placeholder for Candidate Detail (full UI in a later phase)."""
    candidate = mock_candidates.get_candidate(cid)
    if candidate is None:
        abort(404)
    return render_template(
        "candidate_detail.html",
        company=mock_data.COMPANY_NAME,
        candidate=candidate,
    )


@app.route("/styleguide")
def styleguide():
    """Reference page for the UI design system."""
    return render_template(
        "styleguide.html",
        company=mock_data.COMPANY_NAME,
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
