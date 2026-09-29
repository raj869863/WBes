"""Mock data package (UI development only — no real personal data).

Domain datasets live in the submodules:
    mock.candidates   - candidate records and status metadata
    mock.interviews   - upcoming interview records
    mock.activity     - recent recruitment activity

Dashboard-level aggregates are kept here in the package root. All mock
data will be replaced by real data through the services + providers
layers in a later phase.
"""

# --- Dashboard-level mock aggregates (moved from the previous mock_data.py) ---

KPI_CARDS = [
    {
        "label": "Total Candidates",
        "value": 128,
        "hint": "Across all open roles",
        "tone": "teal",
        "icon_path": (
            "M10 4.2a3 3 0 1 1 0 6 3 3 0 0 1 0-6z"
            "M4.5 16.4c.6-2.8 2.9-4.2 5.5-4.2s4.9 1.4 5.5 4.2"
        ),
    },
    {
        "label": "Confirmed Interviews",
        "value": 42,
        "hint": "Scheduled and locked in",
        "tone": "mint",
        "icon_path": (
            "M10 3.2a6.8 6.8 0 1 1 0 13.6 6.8 6.8 0 0 1 0-13.6z"
            "M7.1 10.3l2 2 3.8-4.1"
        ),
    },
    {
        "label": "Upcoming Interviews",
        "value": 18,
        "hint": "In the next 7 days",
        "tone": "blue",
        "icon_path": (
            "M5.5 4h9A1.5 1.5 0 0 1 16 5.5v9a1.5 1.5 0 0 1-1.5 1.5h-9"
            "A1.5 1.5 0 0 1 4 14.5v-9A1.5 1.5 0 0 1 5.5 4zM4 8h12"
            "M6.5 2.5v3M13.5 2.5v3"
        ),
    },
    {
        "label": "No Response",
        "value": 23,
        "hint": "No reply for 5+ days",
        "tone": "coral",
        "icon_path": (
            "M10 3.2a6.8 6.8 0 1 1 0 13.6 6.8 6.8 0 0 1 0-13.6z"
            "M10 6.4v3.8l2.5 1.9"
        ),
    },
]

CANDIDATE_STATUSES = [
    {"label": "Greeted",           "count": 24, "tone": "neutral"},
    {"label": "HR Call Requested", "count": 14, "tone": "warning"},
    {"label": "Date Selected",     "count": 10, "tone": "info"},
    {"label": "Slot Selected",     "count": 8,  "tone": "info"},
    {"label": "Confirmed",         "count": 42, "tone": "success"},
    {"label": "Rescheduled",       "count": 5,  "tone": "warning"},
    {"label": "Cancelled",         "count": 2,  "tone": "neutral"},
    {"label": "No Response",       "count": 23, "tone": "attention"},
]

# Bar width is relative to the largest status count (visual comparison).
_MAX_STATUS_COUNT = max(s["count"] for s in CANDIDATE_STATUSES)
for _s in CANDIDATE_STATUSES:
    _s["pct"] = round(_s["count"] / _MAX_STATUS_COUNT * 100)
