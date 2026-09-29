"""Wissen Baum Engineering Solutions - Internal HR Dashboard.

Phase 0: minimal Flask foundation (GET / smoke test).
Phase 1A: UI design system + /styleguide reference page.
No application features, data connections, or authentication yet.
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


@app.route("/styleguide")
def styleguide():
    """Reference page for the Phase 1A UI design system (not an app page)."""
    return render_template(
        "styleguide.html",
        company="Wissen Baum Engineering Solutions",
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
