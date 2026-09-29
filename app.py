"""Wissen Baum Engineering Solutions - Internal HR Dashboard.

Flask entry point / application factory.

Architecture (target):
    Browser -> Flask routes -> Services -> Provider -> Airtable / MySQL
    Services -> Integrations -> n8n / Google

Currently only routes + mock data exist; services, providers and
integrations are placeholder modules.
"""

from flask import Flask, render_template

import config
from routes import register_routes


def create_app(config_object=config.Config):
    """Create and configure the Flask application."""
    app = Flask(__name__)
    app.config.from_object(config_object)
    register_routes(app)

    # Dev-only design-system reference page (not a business route).
    @app.route("/styleguide")
    def styleguide():
        return render_template("styleguide.html", company=config.COMPANY_NAME)

    return app


app = create_app()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
