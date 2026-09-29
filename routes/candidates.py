"""Candidates routes: /candidates and /candidates/<candidate_id>."""

from flask import Blueprint, abort, render_template

import config
from mock import candidates as candidates_mock

candidates_bp = Blueprint("candidates", __name__)


@candidates_bp.route("/candidates")
def index():
    """Candidates - searchable, filterable HR data table (mock data)."""
    return render_template(
        "candidates/index.html",
        company=config.COMPANY_NAME,
        candidates=candidates_mock.CANDIDATES,
        filters=candidates_mock.filter_options(),
    )


@candidates_bp.route("/candidates/<cid>")
def detail(cid):
    """Minimal placeholder for Candidate Detail (full UI in a later phase)."""
    candidate = candidates_mock.get_candidate(cid)
    if candidate is None:
        abort(404)
    return render_template(
        "candidates/detail.html",
        company=config.COMPANY_NAME,
        candidate=candidate,
    )
