"""Mock recruitment activity / log data (UI development only).

RECENT_ACTIVITY feeds the Dashboard; LOGS is the full audit trail shown on
the Activity / Logs page. Action keys mirror the Airtable-derived log
concepts (message_sent, ics_sent, ...). No real personal data.
"""

# --- Dashboard feed (unchanged shape) ----------------------------------------------

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

# --- Activity / Logs page --------------------------------------------------------

# Airtable-derived action keys -> human-readable label + badge tone
ACTION_META = {
    "message_sent":       {"label": "Message Sent",       "tone": "info"},
    "button_clicked":     {"label": "Button Clicked",     "tone": "neutral"},
    "list_item_selected": {"label": "List Item Selected", "tone": "neutral"},
    "ics_sent":           {"label": "ICS Sent",           "tone": "info"},
    "email_sent":         {"label": "Email Sent",         "tone": "info"},
    "reschedule_initiated": {"label": "Reschedule Initiated", "tone": "warning"},
    "error":              {"label": "Error",              "tone": "attention"},
    "invalid_phone":      {"label": "Invalid Phone",      "tone": "attention"},
    "cooldown_sent":      {"label": "Cooldown Sent",      "tone": "warning"},
    "score_low":          {"label": "Score Low",          "tone": "warning"},
    "duplicate_skipped":  {"label": "Duplicate Skipped",  "tone": "neutral"},
    "candidate_added":    {"label": "Candidate Added",    "tone": "success"},
}

_LOGS_RAW = [
    {"timestamp": "29 Sep 2026, 09:15", "candidate": "Ananya Sharma",   "action": "message_sent",       "details": "Confirmation message sent for interview on 30 Sep, 11:00",        "message_id": "MSG-2909-0142"},
    {"timestamp": "29 Sep 2026, 09:02", "candidate": "Sanjay Rao",      "action": "ics_sent",           "details": "Calendar invite sent for 03 Oct, 11:30 interview",                "message_id": "MSG-2909-0138"},
    {"timestamp": "29 Sep 2026, 08:40", "candidate": "Vikram Iyer",     "action": "message_sent",       "details": "Welcome message sent for Site Survey Engineer",                   "message_id": "MSG-2909-0131"},
    {"timestamp": "29 Sep 2026, 08:12", "candidate": "Imran Shaikh",    "action": "cooldown_sent",      "details": "Follow-up cooldown message sent after 5 days without response",   "message_id": "MSG-2909-0125"},
    {"timestamp": "28 Sep 2026, 18:55", "candidate": "Akash Pawar",     "action": "candidate_added",    "details": "Candidate added from careers inbox for PLC Automation Engineer",  "message_id": "MSG-2809-0119"},
    {"timestamp": "28 Sep 2026, 17:31", "candidate": "Ritika Jain",     "action": "score_low",          "details": "Screening score 42 below threshold 55 for Structural Analyst",   "message_id": "MSG-2809-0114"},
    {"timestamp": "28 Sep 2026, 16:30", "candidate": "Nikhil Joshi",    "action": "list_item_selected", "details": "Selected interview date 06 Oct from offered dates",                "message_id": "MSG-2809-0109"},
    {"timestamp": "28 Sep 2026, 15:47", "candidate": "Karan Verma",     "action": "error",              "details": "Failed to create calendar event: interviewer calendar unavailable", "message_id": "MSG-2809-0104"},
    {"timestamp": "28 Sep 2026, 14:20", "candidate": "Sanika Patil",    "action": "email_sent",         "details": "Interview reminder email sent for 04 Oct, 12:00",                 "message_id": "MSG-2809-0098"},
    {"timestamp": "28 Sep 2026, 11:05", "candidate": "Divya Menon",     "action": "button_clicked",     "details": "Candidate clicked Confirm button for 01 Oct, 16:00 interview",    "message_id": "MSG-2809-0091"},
    {"timestamp": "27 Sep 2026, 18:12", "candidate": "Meera Patil",     "action": "invalid_phone",      "details": "Phone number +91 98200 1000x failed validation on greeting",     "message_id": "MSG-2709-0087"},
    {"timestamp": "27 Sep 2026, 16:44", "candidate": "Arjun Mehta",     "action": "reschedule_initiated", "details": "Candidate requested reschedule from 01 Oct to 02 Oct",             "message_id": "MSG-2709-0082"},
    {"timestamp": "27 Sep 2026, 14:03", "candidate": "Pooja Deshmukh",  "action": "message_sent",       "details": "Interview date options sent for CAD Documentation Specialist",    "message_id": "MSG-2709-0076"},
    {"timestamp": "27 Sep 2026, 11:36", "candidate": "Rahul Menon",     "action": "button_clicked",     "details": "Candidate clicked Select Slot button for 03 Oct, 10:00",          "message_id": "MSG-2709-0071"},
    {"timestamp": "26 Sep 2026, 17:55", "candidate": "Manish Gupta",    "action": "message_sent",       "details": "Interview confirmed message sent for 05 Oct, 14:30",              "message_id": "MSG-2609-0068"},
    {"timestamp": "26 Sep 2026, 15:18", "candidate": "Aditya Kulkarni", "action": "duplicate_skipped",  "details": "Duplicate candidate record skipped (same phone as WB0012)",       "message_id": "MSG-2609-0062"},
    {"timestamp": "26 Sep 2026, 12:41", "candidate": "Sneha Kulkarni",  "action": "list_item_selected", "details": "Selected interview slot 09:30 - 10:15 on 05 Oct",                   "message_id": "MSG-2609-0057"},
    {"timestamp": "26 Sep 2026, 10:12", "candidate": "Ananya Sharma",   "action": "email_sent",         "details": "Confirmation email with ICS attachment sent",                     "message_id": "MSG-2609-0051"},
    {"timestamp": "25 Sep 2026, 19:04", "candidate": "Tanvi Ghosh",     "action": "message_sent",       "details": "HR call requested message sent to recruitment inbox",             "message_id": "MSG-2509-0046"},
    {"timestamp": "25 Sep 2026, 16:40", "candidate": "Rohan Deshpande", "action": "ics_sent",           "details": "Calendar invite sent for 30 Sep, 15:30 interview",                "message_id": "MSG-2509-0042"},
    {"timestamp": "25 Sep 2026, 13:27", "candidate": "Kavya Reddy",     "action": "button_clicked",     "details": "Candidate clicked Request HR Call button",                        "message_id": "MSG-2509-0037"},
    {"timestamp": "25 Sep 2026, 10:53", "candidate": "Ishita Bose",     "action": "message_sent",       "details": "Interview date options sent for Site Survey Engineer",            "message_id": "MSG-2509-0031"},
    {"timestamp": "24 Sep 2026, 17:22", "candidate": "Farhan Sheikh",   "action": "reschedule_initiated", "details": "HR initiated reschedule from 05 Oct to 07 Oct",                   "message_id": "MSG-2409-0026"},
    {"timestamp": "24 Sep 2026, 14:09", "candidate": "Neha Kamath",     "action": "list_item_selected", "details": "Selected interview slot 15:00 - 15:45 on 09 Oct",                   "message_id": "MSG-2409-0021"},
    {"timestamp": "24 Sep 2026, 09:48", "candidate": "Vikram Iyer",     "action": "candidate_added",    "details": "Candidate added from employee referral",                           "message_id": "MSG-2409-0017"},
]

LOGS = []
for _l in _LOGS_RAW:
    _log = dict(_l)
    _log["action_label"] = ACTION_META[_l["action"]]["label"]
    _log["action_tone"] = ACTION_META[_l["action"]]["tone"]
    LOGS.append(_log)


def filter_options():
    """Distinct filter values for the Activity page, as {key: [(value, label)]}."""
    return {
        "action": sorted({(k, m["label"]) for k, m in ACTION_META.items()}),
        "candidate": sorted({(c, c) for c in (l["candidate"] for l in LOGS)}),
    }
