from fastapi import FastAPI
from pydantic import BaseModel
from typing import List, Dict

app = FastAPI(title="AgentZarvis API")

class BriefRequest(BaseModel):
    emails: List[Dict]
    calendar_ics: str
    meeting_text: str

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/brief")
def brief(req: BriefRequest):
    # TODO: replace with real agents; returning stub for now
    return {
        "priorities":[
            {"title":"Send KPI deck","why":"CEO requested by tonight"},
            {"title":"Clear invoice INV-2048","why":"Overdue notice received"}
        ],
        "draft_replies":[
            {"subject":"Board prep",
             "reply":"Hi, attaching KPIs and runway. Please confirm if you need cohort or logo slides as well. —Rajesh"}
        ],
        "plan":[
            {"time":"09:00","item":"Standup"},
            {"time":"10:00","item":"Focus block — KPI deck"},
            {"time":"11:00","item":"Investor call (Zoom)"},
            {"time":"13:00","item":"Lunch + 10-min walk"},
            {"time":"15:00","item":"Customer security review"},
            {"time":"17:30","item":"Gym (30 min)"},
        ],
        "meeting":{
            "summary":"Investor wants MRR, churn, CAC, runway. Follow-up with KPI deck and schedule Friday check-in.",
            "decisions":["Share KPI deck today"],
            "actions":[{"owner":"Rajesh","task":"Send KPI deck","due":"today"}]
        }
    }
