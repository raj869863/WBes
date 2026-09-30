"""Calendar routes: /calendar (HR interview scheduling calendar)."""

import calendar as _calendar
from datetime import date, timedelta

from flask import Blueprint, render_template, request

import config
from mock.interviews import INTERVIEWS

calendar_bp = Blueprint("calendar", __name__)

_WEEKDAYS = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
_MAX_ENTRIES_PER_CELL = 3


def _parse_month(value):
    """Parse a YYYY-MM string into a date (first of month), or None."""
    if not value:
        return None
    try:
        year, month = (int(x) for x in value.split("-"))
        return date(year, month, 1)
    except (ValueError, TypeError):
        return None


def _month_grid(first_of_month):
    """Build the calendar weeks for a month, with interview entries per day."""
    interviews_by_date = {}
    for iv in INTERVIEWS:
        interviews_by_date.setdefault(iv["date"], []).append(iv)

    weeks = []
    for week in _calendar.monthcalendar(first_of_month.year, first_of_month.month):
        days = []
        for day in week:
            if day == 0:
                days.append(None)
                continue
            iso = first_of_month.replace(day=day).isoformat()
            entries = interviews_by_date.get(iso, [])
            days.append({
                "day": day,
                "iso": iso,
                "entries": entries,
                "extra": max(0, len(entries) - _MAX_ENTRIES_PER_CELL),
            })
        weeks.append(days)
    return weeks


@calendar_bp.route("/calendar")
def index():
    """HR interview scheduling calendar (mock data)."""
    from flask import request

    today = date.today()
    month = _parse_month(request.args.get("month"))
    if month is None:
        month = today.replace(day=1)

    prev_month = (month - timedelta(days=1)).replace(day=1)
    next_month = (month + timedelta(days=32)).replace(day=1)

    month_prefix = month.strftime("%Y-%m")
    month_entries = sorted(
        (i for i in INTERVIEWS if i["date"].startswith(month_prefix)),
        key=lambda i: (i["date"], i["slot"]),
    )

    return render_template(
        "calendar/index.html",
        company=config.COMPANY_NAME,
        weeks=_month_grid(month),
        weekdays=_WEEKDAYS,
        month_label=month.strftime("%B %Y"),
        prev_month=prev_month.strftime("%Y-%m"),
        next_month=next_month.strftime("%Y-%m"),
        current_month=today.strftime("%Y-%m"),
        is_current_month=month == today.replace(day=1),
        # Flat, date-ordered list for the displayed month (mobile/day view)
        entries=month_entries,
    )
