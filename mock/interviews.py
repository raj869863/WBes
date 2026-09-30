"""Mock interview data (UI development only).

INTERVIEWS is the full interview model used by the Interviews and Calendar
pages. UPCOMING_INTERVIEWS is a projection of the same records used by the
Dashboard (kept shape-compatible with the original dashboard mock data).

No real personal data.
"""

from datetime import date as _date

# Interviews page status vocabulary -> badge tone
STATUS_TONES = {
    "Confirmed": "success",
    "Upcoming": "info",
    "Rescheduled": "warning",
    "Cancelled": "attention",
    "Completed": "neutral",
}

def _fmt_date(iso):
    y, m, d = (int(x) for x in iso.split("-"))
    return _date(y, m, d).strftime("%d %b %Y")

# --- Full interview records -------------------------------------------------------
# One record per candidate with a scheduled/current or past interview.
# meet_url / event_id / confirmed_at exist only for confirmed interviews.

_INTERVIEW_RAW = [
    # Current / upcoming
    {"cid": "WB0001", "candidate": "Ananya Sharma",   "role": "CAE Engineer",                 "jd_code": "JD-CAE-101", "date": "2026-09-30", "slot": "11:00 - 11:45", "interviewer": "S. Raghavan",     "status": "Confirmed",   "meet_url": "https://meet.google.com/mock-aqb-wxz", "event_id": "evt_wb0001_930", "confirmed_at": "26 Sep 2026, 10:12"},
    {"cid": "WB0002", "candidate": "Rohan Deshpande", "role": "HVAC Project Engineer",        "jd_code": "JD-HPE-107", "date": "2026-09-30", "slot": "15:30 - 16:15", "interviewer": "Meera Kulkarni",   "status": "Confirmed",   "meet_url": "https://meet.google.com/mock-jtd-fpu", "event_id": "evt_wb0002_930", "confirmed_at": "25 Sep 2026, 16:40"},
    {"cid": "WB0003", "candidate": "Priya Nair",      "role": "Structural Analyst",           "jd_code": "JD-STR-120", "date": "2026-10-01", "slot": "10:00 - 10:45", "interviewer": "Pooja Bhat",       "status": "Upcoming",    "meet_url": None, "event_id": None, "confirmed_at": None},
    {"cid": "WB0004", "candidate": "Arjun Mehta",     "role": "PLC Automation Engineer",      "jd_code": "JD-PAE-110", "date": "2026-10-02", "slot": "14:00 - 14:45", "interviewer": "S. Raghavan",     "status": "Rescheduled", "meet_url": "https://meet.google.com/mock-kev-rsm", "event_id": "evt_wb0004_1002", "confirmed_at": "27 Sep 2026, 11:05"},
    {"cid": "WB0005", "candidate": "Sneha Kulkarni",  "role": "CAD Documentation Specialist", "jd_code": "JD-CDS-113", "date": "2026-10-05", "slot": "09:30 - 10:15", "interviewer": "Meera Kulkarni",   "status": "Upcoming",    "meet_url": None, "event_id": None, "confirmed_at": None},
    {"cid": "WB0008", "candidate": "Nikhil Joshi",    "role": "Electrical Design Engineer",   "jd_code": "JD-EDE-104", "date": "2026-10-06", "slot": "",             "interviewer": "Pooja Bhat",       "status": "Upcoming",    "meet_url": None, "event_id": None, "confirmed_at": None},
    {"cid": "WB0010", "candidate": "Sanjay Rao",      "role": "PLC Automation Engineer",      "jd_code": "JD-PAE-110", "date": "2026-10-03", "slot": "11:30 - 12:15", "interviewer": "S. Raghavan",     "status": "Confirmed",   "meet_url": "https://meet.google.com/mock-qwe-rty", "event_id": "evt_wb0010_1003", "confirmed_at": "28 Sep 2026, 09:30"},
    {"cid": "WB0011", "candidate": "Divya Menon",     "role": "Structural Analyst",           "jd_code": "JD-STR-120", "date": "2026-10-01", "slot": "16:00 - 16:45", "interviewer": "Pooja Bhat",       "status": "Confirmed",   "meet_url": "https://meet.google.com/mock-asd-fgh", "event_id": "evt_wb0011_1001", "confirmed_at": "26 Sep 2026, 14:22"},
    {"cid": "WB0013", "candidate": "Farhan Sheikh",   "role": "Electrical Design Engineer",   "jd_code": "JD-EDE-104", "date": "2026-10-07", "slot": "10:30 - 11:15", "interviewer": "Meera Kulkarni",   "status": "Rescheduled", "meet_url": "https://meet.google.com/mock-zxc-vbn", "event_id": "evt_wb0013_1007", "confirmed_at": "24 Sep 2026, 18:03"},
    {"cid": "WB0014", "candidate": "Ishita Bose",     "role": "Site Survey Engineer",         "jd_code": "JD-SSE-118", "date": "2026-10-08", "slot": "",             "interviewer": "Vikas Ranade",     "status": "Upcoming",    "meet_url": None, "event_id": None, "confirmed_at": None},
    {"cid": "WB0017", "candidate": "Neha Kamath",     "role": "PLC Automation Engineer",      "jd_code": "JD-PAE-110", "date": "2026-10-09", "slot": "15:00 - 15:45", "interviewer": "S. Raghavan",     "status": "Upcoming",    "meet_url": None, "event_id": None, "confirmed_at": None},
    {"cid": "WB0018", "candidate": "Rahul Menon",     "role": "CAE Engineer",                 "jd_code": "JD-CAE-101", "date": "2026-10-03", "slot": "10:00 - 10:45", "interviewer": "Pooja Bhat",       "status": "Confirmed",   "meet_url": "https://meet.google.com/mock-ijk-lmn", "event_id": "evt_wb0018_1003", "confirmed_at": "27 Sep 2026, 12:45"},
    {"cid": "WB0019", "candidate": "Sanika Patil",    "role": "Electrical Design Engineer",   "jd_code": "JD-EDE-104", "date": "2026-10-04", "slot": "12:00 - 12:45", "interviewer": "Meera Kulkarni",   "status": "Confirmed",   "meet_url": "https://meet.google.com/mock-opq-rst", "event_id": "evt_wb0019_1004", "confirmed_at": "28 Sep 2026, 10:18"},
    {"cid": "WB0022", "candidate": "Manish Gupta",    "role": "HVAC Project Engineer",        "jd_code": "JD-HPE-107", "date": "2026-10-05", "slot": "14:30 - 15:15", "interviewer": "Vikas Ranade",     "status": "Confirmed",   "meet_url": "https://meet.google.com/mock-uvw-xyz", "event_id": "evt_wb0022_1005", "confirmed_at": "26 Sep 2026, 17:55"},
    {"cid": "WB0023", "candidate": "Pooja Deshmukh",  "role": "CAD Documentation Specialist", "jd_code": "JD-CDS-113", "date": "2026-10-10", "slot": "",             "interviewer": "Meera Kulkarni",   "status": "Upcoming",    "meet_url": None, "event_id": None, "confirmed_at": None},
    # Past / completed / cancelled
    {"cid": "WB0006", "candidate": "Vikram Iyer",     "role": "Site Survey Engineer",         "jd_code": "JD-SSE-118", "date": "2026-09-24", "slot": "11:00 - 11:45", "interviewer": "Vikas Ranade",     "status": "Completed",   "meet_url": None, "event_id": None, "confirmed_at": "22 Sep 2026, 09:00"},
    {"cid": "WB0009", "candidate": "Meera Patil",     "role": "HVAC Project Engineer",        "jd_code": "JD-HPE-107", "date": "2026-09-25", "slot": "10:00 - 10:45", "interviewer": "Meera Kulkarni",   "status": "Completed",   "meet_url": None, "event_id": None, "confirmed_at": "23 Sep 2026, 15:30"},
    {"cid": "WB0012", "candidate": "Aditya Kulkarni", "role": "CAD Documentation Specialist", "jd_code": "JD-CDS-113", "date": "2026-09-22", "slot": "14:00 - 14:45", "interviewer": "Meera Kulkarni",   "status": "Completed",   "meet_url": None, "event_id": None, "confirmed_at": "20 Sep 2026, 11:20"},
    {"cid": "WB0015", "candidate": "Karan Verma",     "role": "CAE Engineer",                 "jd_code": "JD-CAE-101", "date": "2026-09-28", "slot": "15:30 - 16:15", "interviewer": "Pooja Bhat",       "status": "Cancelled",   "meet_url": None, "event_id": None, "confirmed_at": None},
    {"cid": "WB0016", "candidate": "Tanvi Ghosh",     "role": "HVAC Project Engineer",        "jd_code": "JD-HPE-107", "date": "2026-09-26", "slot": "11:30 - 12:15", "interviewer": "Vikas Ranade",     "status": "Completed",   "meet_url": None, "event_id": None, "confirmed_at": "24 Sep 2026, 13:10"},
    {"cid": "WB0020", "candidate": "Imran Shaikh",    "role": "Site Survey Engineer",         "jd_code": "JD-SSE-118", "date": "2026-09-23", "slot": "16:00 - 16:45", "interviewer": "S. Raghavan",     "status": "Completed",   "meet_url": None, "event_id": None, "confirmed_at": "21 Sep 2026, 10:40"},
    {"cid": "WB0021", "candidate": "Ritika Jain",     "role": "Structural Analyst",           "jd_code": "JD-STR-120", "date": "2026-09-25", "slot": "15:00 - 15:45", "interviewer": "Pooja Bhat",       "status": "Completed",   "meet_url": None, "event_id": None, "confirmed_at": "23 Sep 2026, 09:55"},
    {"cid": "WB0024", "candidate": "Akash Pawar",     "role": "PLC Automation Engineer",      "jd_code": "JD-PAE-110", "date": "2026-09-24", "slot": "12:00 - 12:45", "interviewer": "S. Raghavan",     "status": "Completed",   "meet_url": None, "event_id": None, "confirmed_at": "22 Sep 2026, 16:05"},
]

INTERVIEWS = []
for _r in _INTERVIEW_RAW:
    _i = dict(_r)
    _i["date_label"] = _fmt_date(_i["date"])
    _i["status_tone"] = STATUS_TONES[_i["status"]]
    INTERVIEWS.append(_i)


def get_interview(cid):
    """Return the interview record for a candidate ID, or None."""
    cid = (cid or "").upper()
    return next((i for i in INTERVIEWS if i["cid"] == cid), None)


def filter_options():
    """Distinct filter values for the Interviews page, as {key: [(value, label)]}."""
    def uniq(key):
        return sorted({i[key] for i in INTERVIEWS if i[key]})

    return {
        "status": [(s, s) for s in STATUS_TONES],
        "role": [(v, v) for v in uniq("role")],
        "interviewer": [(v, v) for v in uniq("interviewer")],
        "date": [(v, _fmt_date(v)) for v in uniq("date")],
        "slot": [(v, v) for v in uniq("slot")],
    }


# --- Dashboard projection ----------------------------------------------------------
# Same records, projected to the shape the Dashboard template expects.

_DASHBOARD_STATUS_LABELS = {"Upcoming": "Slot Selected"}

UPCOMING_INTERVIEWS = [
    {
        "candidate": i["candidate"],
        "role": i["role"],
        "date": i["date_label"],
        "slot": i["slot"],
        "interviewer": i["interviewer"],
        "status": _DASHBOARD_STATUS_LABELS.get(i["status"], i["status"]),
        "status_tone": i["status_tone"],
        "meet_url": i["meet_url"],
    }
    for i in INTERVIEWS
    if i["cid"] in ("WB0001", "WB0002", "WB0003", "WB0004", "WB0005")
]
