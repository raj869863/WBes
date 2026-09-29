"""Route blueprints for the HR dashboard.

Future routes:
    / , /dashboard , /candidates , /candidates/<candidate_id> ,
    /calendar , /interviews , /jobs , /activity

Dashboard and Candidates are implemented; Calendar, Interviews, Jobs and
Activity blueprints are structure placeholders with no routes yet.
"""

from .activity import activity_bp
from .calendar import calendar_bp
from .candidates import candidates_bp
from .dashboard import dashboard_bp
from .interviews import interviews_bp
from .jobs import jobs_bp

__all__ = [
    "activity_bp",
    "calendar_bp",
    "candidates_bp",
    "dashboard_bp",
    "interviews_bp",
    "jobs_bp",
]


def register_routes(app):
    """Register all route blueprints on the Flask application."""
    app.register_blueprint(dashboard_bp)
    app.register_blueprint(candidates_bp)
    # Placeholder blueprints — no routes defined yet (pages come later).
    app.register_blueprint(calendar_bp)
    app.register_blueprint(interviews_bp)
    app.register_blueprint(jobs_bp)
    app.register_blueprint(activity_bp)
