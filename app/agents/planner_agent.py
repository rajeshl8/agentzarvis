from datetime import datetime, timedelta

def build_plan(calendar_ics: str) -> list[dict]:
    """Very naive plan from ICS; replace with proper ICS parsing later."""
    # Stub: returns two fixed blocks plus a meeting placeholder
    return [
        {"time":"09:00","item":"Standup"},
        {"time":"10:00","item":"Focus block — deep work"},
        {"time":"15:00","item":"Customer meeting"}
    ]
