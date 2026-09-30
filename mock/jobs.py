"""Mock job / JD data (UI development only).

Candidate counts are derived from the mock candidate dataset so the pages
stay consistent. No real data.
"""

from mock.candidates import CANDIDATES

# Status vocabulary -> badge tone
STATUS_TONES = {
    "Open": "success",
    "On Hold": "warning",
    "Closed": "neutral",
}

_JOBS_RAW = [
    {"jd_code": "JD-CAE-101", "role": "CAE Engineer",                 "area": "Engineering",    "status": "Open",     "tool_test": "Required",     "description": "FEA/CFD analysis for engineering projects; simulation and validation work.", "has_document": True},
    {"jd_code": "JD-EDE-104", "role": "Electrical Design Engineer",   "area": "Engineering",    "status": "Open",     "tool_test": "Required",     "description": "Electrical system design, schematics and load calculations for industrial projects.", "has_document": True},
    {"jd_code": "JD-HPE-107", "role": "HVAC Project Engineer",        "area": "Projects",       "status": "Open",     "tool_test": "Not Required", "description": "HVAC design and project execution; site coordination and vendor management.", "has_document": True},
    {"jd_code": "JD-CDS-113", "role": "CAD Documentation Specialist", "area": "Documentation",  "status": "Open",     "tool_test": "Not Required", "description": "CAD drafting, drawing standards and technical documentation support.", "has_document": False},
    {"jd_code": "JD-PAE-110", "role": "PLC Automation Engineer",      "area": "Engineering",    "status": "Open",     "tool_test": "Required",     "description": "PLC programming, control panel design and factory automation support.", "has_document": True},
    {"jd_code": "JD-STR-120", "role": "Structural Analyst",           "area": "Engineering",    "status": "On Hold",  "tool_test": "Not Required", "description": "Structural analysis and design verification for industrial structures.", "has_document": True},
    {"jd_code": "JD-SSE-118", "role": "Site Survey Engineer",         "area": "Field Services", "status": "Open",     "tool_test": "Not Required", "description": "Site surveys, data collection and condition assessment reports.", "has_document": False},
    {"jd_code": "JD-PMT-131", "role": "Project Management Trainee",   "area": "Projects",       "status": "Closed",   "tool_test": "Not Required", "description": "Trainee role supporting project planning, tracking and reporting.", "has_document": True},
]


def _candidate_count(jd_code):
    return sum(1 for c in CANDIDATES if c["jd_code"] == jd_code)


JOBS = []
for _j in _JOBS_RAW:
    _job = dict(_j)
    _job["candidate_count"] = _candidate_count(_job["jd_code"])
    _job["status_tone"] = STATUS_TONES[_job["status"]]
    JOBS.append(_job)


def filter_options():
    """Distinct filter values for the Jobs page, as {key: [(value, label)]}."""
    return {
        "area": sorted({(j["area"], j["area"]) for j in JOBS}),
        "role": sorted({(j["role"], j["role"]) for j in JOBS}),
        "status": [(s, s) for s in STATUS_TONES],
    }
