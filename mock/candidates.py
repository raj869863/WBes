"""Mock candidate data for the Candidates page (WBes internal HR dashboard).

UI-only mock data, isolated here so it can later be replaced by the real
data provider (Airtable/MySQL via the services/providers layers). No real
personal data.
"""

from datetime import date as _date

# --- Status metadata (key -> label + badge tone) --------------------------------
# Keys match the candidate statuses used by the pipeline.

STATUS_META = {
    "greeted":           {"label": "Greeted",           "tone": "neutral"},
    "hr_call_requested": {"label": "HR Call Requested", "tone": "warning"},
    "date_selected":     {"label": "Date Selected",     "tone": "info"},
    "slot_selected":     {"label": "Slot Selected",     "tone": "info"},
    "confirmed":         {"label": "Confirmed",         "tone": "success"},
    "rescheduled":       {"label": "Rescheduled",       "tone": "warning"},
    "cancelled":         {"label": "Cancelled",         "tone": "neutral"},
    "no_response":       {"label": "No Response",       "tone": "attention"},
}

EXPERIENCE_BUCKETS = ["0-2 yrs", "2-5 yrs", "5-8 yrs", "8+ yrs"]


def _experience_bucket(years):
    if years < 2:
        return "0-2 yrs"
    if years < 5:
        return "2-5 yrs"
    if years < 8:
        return "5-8 yrs"
    return "8+ yrs"


def _fmt_date(iso):
    y, m, d = (int(x) for x in iso.split("-"))
    return _date(y, m, d).strftime("%d %b %Y")


# --- Raw mock candidates ----------------------------------------------------------
# interview_date is ISO (empty string when not scheduled).

_RAW = [
    {"name": "Ananya Sharma",   "cid": "WB-1001", "role": "CAE Engineer",                 "jd_code": "JD-CAE-101", "status": "confirmed",         "interview_date": "2026-09-30", "slot": "11:00 - 11:45", "experience": 6.5, "track": "Analysis",     "tool_test": "Required",     "processed": True,  "phone": "+91 98200 10001", "email": "ananya.sharma@example.com"},
    {"name": "Rohan Deshpande", "cid": "WB-1002", "role": "HVAC Project Engineer",        "jd_code": "JD-HPE-107", "status": "confirmed",         "interview_date": "2026-09-30", "slot": "15:30 - 16:15", "experience": 8.0, "track": "Projects",     "tool_test": "Not Required", "processed": True,  "phone": "+91 98200 10002", "email": "rohan.deshpande@example.com"},
    {"name": "Priya Nair",      "cid": "WB-1003", "role": "Structural Analyst",           "jd_code": "JD-STR-120", "status": "slot_selected",     "interview_date": "2026-10-01", "slot": "10:00 - 10:45", "experience": 4.0, "track": "Analysis",     "tool_test": "Required",     "processed": False, "phone": "+91 98200 10003", "email": "priya.nair@example.com"},
    {"name": "Arjun Mehta",     "cid": "WB-1004", "role": "PLC Automation Engineer",      "jd_code": "JD-PAE-110", "status": "rescheduled",       "interview_date": "2026-10-02", "slot": "14:00 - 14:45", "experience": 5.5, "track": "Automation",   "tool_test": "Required",     "processed": True,  "phone": "+91 98200 10004", "email": "arjun.mehta@example.com"},
    {"name": "Sneha Kulkarni",  "cid": "WB-1005", "role": "CAD Documentation Specialist", "jd_code": "JD-CDS-113", "status": "slot_selected",     "interview_date": "2026-10-05", "slot": "09:30 - 10:15", "experience": 3.0, "track": "Documentation", "tool_test": "Not Required", "processed": False, "phone": "+91 98200 10005", "email": "sneha.kulkarni@example.com"},
    {"name": "Vikram Iyer",     "cid": "WB-1006", "role": "Site Survey Engineer",         "jd_code": "JD-SSE-118", "status": "greeted",           "interview_date": "",           "slot": "",             "experience": 2.5, "track": "Site",         "tool_test": "Not Required", "processed": False, "phone": "+91 98200 10006", "email": "vikram.iyer@example.com"},
    {"name": "Kavya Reddy",     "cid": "WB-1007", "role": "CAE Engineer",                 "jd_code": "JD-CAE-101", "status": "hr_call_requested", "interview_date": "",           "slot": "",             "experience": 7.0, "track": "Analysis",     "tool_test": "Required",     "processed": False, "phone": "+91 98200 10007", "email": "kavya.reddy@example.com"},
    {"name": "Nikhil Joshi",    "cid": "WB-1008", "role": "Electrical Design Engineer",   "jd_code": "JD-EDE-104", "status": "date_selected",     "interview_date": "2026-10-06", "slot": "",             "experience": 4.5, "track": "Design",       "tool_test": "Required",     "processed": False, "phone": "+91 98200 10008", "email": "nikhil.joshi@example.com"},
    {"name": "Meera Patil",     "cid": "WB-1009", "role": "HVAC Project Engineer",        "jd_code": "JD-HPE-107", "status": "no_response",       "interview_date": "",           "slot": "",             "experience": 6.0, "track": "Projects",     "tool_test": "Not Required", "processed": False, "phone": "+91 98200 10009", "email": "meera.patil@example.com"},
    {"name": "Sanjay Rao",      "cid": "WB-1010", "role": "PLC Automation Engineer",      "jd_code": "JD-PAE-110", "status": "confirmed",         "interview_date": "2026-10-03", "slot": "11:30 - 12:15", "experience": 9.0, "track": "Automation",   "tool_test": "Required",     "processed": True,  "phone": "+91 98200 10010", "email": "sanjay.rao@example.com"},
    {"name": "Divya Menon",     "cid": "WB-1011", "role": "Structural Analyst",           "jd_code": "JD-STR-120", "status": "confirmed",         "interview_date": "2026-10-01", "slot": "16:00 - 16:45", "experience": 3.5, "track": "Analysis",     "tool_test": "Not Required", "processed": True,  "phone": "+91 98200 10011", "email": "divya.menon@example.com"},
    {"name": "Aditya Kulkarni", "cid": "WB-1012", "role": "CAD Documentation Specialist", "jd_code": "JD-CDS-113", "status": "greeted",           "interview_date": "",           "slot": "",             "experience": 1.5, "track": "Documentation", "tool_test": "Not Required", "processed": False, "phone": "+91 98200 10012", "email": "aditya.kulkarni@example.com"},
    {"name": "Farhan Sheikh",   "cid": "WB-1013", "role": "Electrical Design Engineer",   "jd_code": "JD-EDE-104", "status": "rescheduled",       "interview_date": "2026-10-07", "slot": "10:30 - 11:15", "experience": 5.0, "track": "Design",       "tool_test": "Required",     "processed": False, "phone": "+91 98200 10013", "email": "farhan.sheikh@example.com"},
    {"name": "Ishita Bose",     "cid": "WB-1014", "role": "Site Survey Engineer",         "jd_code": "JD-SSE-118", "status": "date_selected",     "interview_date": "2026-10-08", "slot": "",             "experience": 2.0, "track": "Site",         "tool_test": "Not Required", "processed": False, "phone": "+91 98200 10014", "email": "ishita.bose@example.com"},
    {"name": "Karan Verma",     "cid": "WB-1015", "role": "CAE Engineer",                 "jd_code": "JD-CAE-101", "status": "cancelled",         "interview_date": "",           "slot": "",             "experience": 8.5, "track": "Analysis",     "tool_test": "Required",     "processed": True,  "phone": "+91 98200 10015", "email": "karan.verma@example.com"},
    {"name": "Tanvi Ghosh",     "cid": "WB-1016", "role": "HVAC Project Engineer",        "jd_code": "JD-HPE-107", "status": "hr_call_requested", "interview_date": "",           "slot": "",             "experience": 3.8, "track": "Projects",     "tool_test": "Not Required", "processed": False, "phone": "+91 98200 10016", "email": "tanvi.ghosh@example.com"},
    {"name": "Neha Kamath",     "cid": "WB-1017", "role": "PLC Automation Engineer",      "jd_code": "JD-PAE-110", "status": "slot_selected",     "interview_date": "2026-10-09", "slot": "15:00 - 15:45", "experience": 4.2, "track": "Automation",   "tool_test": "Required",     "processed": False, "phone": "+91 98200 10017", "email": "neha.kamath@example.com"},
]

# --- Decorated candidates (display fields added) -----------------------------------

CANDIDATES = []
for _raw in _RAW:
    _c = dict(_raw)
    _c["date_label"] = _fmt_date(_c["interview_date"]) if _c["interview_date"] else "—"
    _c["experience_bucket"] = _experience_bucket(_c["experience"])
    _c["status_label"] = STATUS_META[_c["status"]]["label"]
    _c["status_tone"] = STATUS_META[_c["status"]]["tone"]
    CANDIDATES.append(_c)


def get_candidate(cid):
    """Return a mock candidate by ID (case-insensitive), or None."""
    cid = (cid or "").upper()
    return next((c for c in CANDIDATES if c["cid"] == cid), None)


def filter_options():
    """Distinct filter values for the Candidates page, as {key: [(value, label)]}."""
    def uniq(key):
        return sorted({c[key] for c in CANDIDATES if c[key]})

    buckets_in_use = {c["experience_bucket"] for c in CANDIDATES}

    return {
        "status": [(key, meta["label"]) for key, meta in STATUS_META.items()],
        "role": [(v, v) for v in uniq("role")],
        "jd_code": [(v, v) for v in uniq("jd_code")],
        "track": [(v, v) for v in uniq("track")],
        "interview_date": [(v, _fmt_date(v)) for v in uniq("interview_date")],
        "slot": [(v, v) for v in uniq("slot")],
        "experience": [(b, b) for b in EXPERIENCE_BUCKETS if b in buckets_in_use],
        "tool_test": [("Required", "Required"), ("Not Required", "Not Required")],
        "processed": [("yes", "Processed"), ("no", "Not processed")],
    }
