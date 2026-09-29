"""Application configuration.

Values are read from environment variables (see .env.example) so no
credentials live in code. Integration keys are placeholders only —
no external service is connected yet.
"""

import os

COMPANY_NAME = "Wissen Baum Engineering Solutions"


class Config:
    """Base configuration object."""

    SECRET_KEY = os.environ.get("SECRET_KEY", "dev-only-not-secret")

    # Future data providers (placeholders — not connected yet)
    AIRTABLE_API_KEY = os.environ.get("AIRTABLE_API_KEY", "")
    AIRTABLE_BASE_ID = os.environ.get("AIRTABLE_BASE_ID", "")
    MYSQL_HOST = os.environ.get("MYSQL_HOST", "")
    MYSQL_PORT = os.environ.get("MYSQL_PORT", "3306")
    MYSQL_USER = os.environ.get("MYSQL_USER", "")
    MYSQL_PASSWORD = os.environ.get("MYSQL_PASSWORD", "")
    MYSQL_DB = os.environ.get("MYSQL_DB", "")

    # Future integrations (placeholders — not connected yet)
    N8N_WEBHOOK_URL = os.environ.get("N8N_WEBHOOK_URL", "")
