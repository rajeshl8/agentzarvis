from fastapi import APIRouter, Body
from typing import Dict, List
from app.agents.planner_agent import PlannerAgent
from app.agents.action_agent import ActionAgent
from app.agents.monitor_agent import MonitorAgent
from app.agents.summary_agent import SummaryAgent
from app.utils.s3_utils import load_demo_data

router = APIRouter()

@router.post("/brief")
def generate_brief():
    emails, calendar_ics, meeting_txt, profile = load_demo_data()
    plan = PlannerAgent().generate_plan(emails, calendar_ics, meeting_txt, profile)
    view = [{"id": t["id"], "task": t["task"], "approved": False} for t in plan]
    return {"daily_plan": view}

@router.post("/brief/confirm")
def confirm_brief(payload: Dict = Body(...)):
    approved: List[Dict] = payload.get("approved", [])
    actions = ActionAgent().execute_plan(approved)
    verify = MonitorAgent().verify_progress([{"status":"done"} for _ in approved])
    summary = SummaryAgent().generate_summary({
        "steps": 7820, "calories_burned": 520, "calories_added": 1780,
        "meetings_done": 4, "productivity": "93%"
    })
    return {"actions": actions, "verify": verify, "summary": summary}
