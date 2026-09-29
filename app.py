"""Wissen Baum Engineering Solutions - Internal HR Dashboard.

Phase 0: minimal Flask foundation. No UI pages, features, or data
connections yet.
"""

from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    """Minimal smoke-test route: proves Flask -> Jinja -> HTML works."""
    return render_template(
        "index.html",
        company="Wissen Baum Engineering Solutions",
        phase="Phase 0 - Project Foundation",
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
