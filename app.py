"""Wissen Baum Engineering Solutions - Internal HR Dashboard.

Phase 0: minimal Flask foundation.
Phase 1A: UI design system (+ /styleguide reference page).
Phase 2: Dashboard page (UI only, mock data - no external services yet).
"""

from flask import Flask, render_template

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


@app.route("/styleguide")
def styleguide():
    """Reference page for the UI design system."""
    return render_template(
        "styleguide.html",
        company=mock_data.COMPANY_NAME,
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
