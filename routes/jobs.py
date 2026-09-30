"""Jobs / JDs routes: /jobs (read-only job description list)."""

from flask import Blueprint, render_template

import config
from mock.jobs import JOBS, filter_options

jobs_bp = Blueprint("jobs", __name__)


@jobs_bp.route("/jobs")
def index():
    """Jobs / JDs - read-only list of job descriptions (mock data)."""
    return render_template(
        "jobs/index.html",
        company=config.COMPANY_NAME,
        jobs=JOBS,
        filters=filter_options(),
    )
