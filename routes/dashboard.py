"""Dashboard routes: / and /dashboard."""

from flask import Blueprint, render_template

import config
from mock import CANDIDATE_STATUSES, KPI_CARDS
from mock.activity import RECENT_ACTIVITY
from mock.interviews import UPCOMING_INTERVIEWS

dashboard_bp = Blueprint("dashboard", __name__)


@dashboard_bp.route("/")
@dashboard_bp.route("/dashboard")
def index():
    """Dashboard - recruitment & interview operations overview (mock data)."""
    return render_template(
        "dashboard/index.html",
        company=config.COMPANY_NAME,
        kpis=KPI_CARDS,
        statuses=CANDIDATE_STATUSES,
        upcoming=UPCOMING_INTERVIEWS,
        activity=RECENT_ACTIVITY,
    )
