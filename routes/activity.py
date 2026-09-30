"""Activity / Logs routes: /activity (read-only audit trail)."""

from flask import Blueprint, render_template

import config
from mock.activity import LOGS, filter_options

activity_bp = Blueprint("activity", __name__)


@activity_bp.route("/activity")
def index():
    """Activity / Logs - recruitment workflow activity and system events."""
    return render_template(
        "activity/index.html",
        company=config.COMPANY_NAME,
        logs=LOGS,
        filters=filter_options(),
    )
