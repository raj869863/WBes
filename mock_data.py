"""Phase 2 mock data for the Dashboard page (WBes internal HR dashboard).

This is UI-only mock data. Keep it clearly separated here so it can be
replaced by real backend data (Airtable/MySQL via a service layer) later.
"""

COMPANY_NAME = "Wissen Baum Engineering Solutions"

# --- Section 1: KPI cards -----------------------------------------------------
# icon_path = single SVG path (20x20 viewBox), rendered inside a small badge.

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

# --- Section 2: Candidate status overview -------------------------------------
# tone maps to badge/fill classes in the design system.

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

# --- Section 3: Upcoming interviews --------------------------------------------
# meet_url: only rows with a Meet link show the action.

UPCOMING_INTERVIEWS = [
    {
        "candidate": "Ananya Sharma",
        "role": "Electrical Design Engineer",
        "date": "30 Sep 2026",
        "slot": "11:00 - 11:45",
        "interviewer": "S. Raghavan",
        "status": "Confirmed",
        "status_tone": "success",
        "meet_url": "https://meet.google.com/mock-aqb-wxz",
    },
    {
        "candidate": "Rohan Deshpande",
        "role": "HVAC Project Engineer",
        "date": "30 Sep 2026",
        "slot": "15:30 - 16:15",
        "interviewer": "Meera Kulkarni",
        "status": "Confirmed",
        "status_tone": "success",
        "meet_url": "https://meet.google.com/mock-jtd-fpu",
    },
    {
        "candidate": "Priya Nair",
        "role": "Structural Analyst",
        "date": "01 Oct 2026",
        "slot": "10:00 - 10:45",
        "interviewer": "Pooja Bhat",
        "status": "Slot Selected",
        "status_tone": "info",
        "meet_url": None,
    },
    {
        "candidate": "Arjun Mehta",
        "role": "PLC Automation Engineer",
        "date": "02 Oct 2026",
        "slot": "14:00 - 14:45",
        "interviewer": "S. Raghavan",
        "status": "Rescheduled",
        "status_tone": "warning",
        "meet_url": "https://meet.google.com/mock-kev-rsm",
    },
    {
        "candidate": "Sneha Kulkarni",
        "role": "CAD Documentation Specialist",
        "date": "05 Oct 2026",
        "slot": "09:30 - 10:15",
        "interviewer": "Meera Kulkarni",
        "status": "Slot Selected",
        "status_tone": "info",
        "meet_url": None,
    },
]

# --- Section 4: Recent activity --------------------------------------------------

RECENT_ACTIVITY = [
    {
        "time": "Today, 09:15",
        "candidate": "Ananya Sharma",
        "action": "Confirmed",
        "action_tone": "success",
        "details": "Interview confirmed for 30 Sep, 11:00 with S. Raghavan",
    },
    {
        "time": "Today, 08:40",
        "candidate": "Vikram Iyer",
        "action": "Greeted",
        "action_tone": "neutral",
        "details": "Welcome message sent for Site Survey Engineer",
    },
    {
        "time": "Yesterday, 17:22",
        "candidate": "Arjun Mehta",
        "action": "Rescheduled",
        "action_tone": "warning",
        "details": "Moved from 01 Oct to 02 Oct, 14:00 at candidate request",
    },
    {
        "time": "Yesterday, 15:05",
        "candidate": "Priya Nair",
        "action": "Slot Selected",
        "action_tone": "info",
        "details": "Picked 01 Oct, 10:00 - 10:45 with Pooja Bhat",
    },
    {
        "time": "Yesterday, 11:48",
        "candidate": "Kavya Reddy",
        "action": "Reminder Sent",
        "action_tone": "neutral",
        "details": "Follow-up reminder sent - HR call requested 4 days ago",
    },
    {
        "time": "28 Sep, 16:30",
        "candidate": "Nikhil Joshi",
        "action": "Date Selected",
        "action_tone": "info",
        "details": "Selected 06 Oct for Electrical Design Engineer interview",
    },
]
