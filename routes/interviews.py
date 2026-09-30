"""Interviews routes: /interviews (operational interview list)."""

from flask import Blueprint, render_template

import config
from mock.interviews import INTERVIEWS, filter_options

interviews_bp = Blueprint("interviews", __name__)


@interviews_bp.route("/interviews")
def index():
    """Interviews - searchable, filterable operational list (mock data)."""
    return render_template(
        "interviews/index.html",
        company=config.COMPANY_NAME,
        interviews=INTERVIEWS,
        filters=filter_options(),
    )
