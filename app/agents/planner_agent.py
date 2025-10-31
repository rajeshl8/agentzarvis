from typing import List, Dict

class PlannerAgent:
    def generate_plan(self, emails: List[Dict], calendar_ics: str, notes: str, profile: Dict) -> List[Dict]:
        plan = [
            {"id":"t1","task":"Gym at 5:30 AM (45m)","status":"pending","category":"health"},
            {"id":"t2","task":"Order Protein Shake (post-workout)","status":"pending","category":"health"},
            {"id":"t3","task":"Meeting Summary — key notes ready","status":"pending","category":"work"},
            {"id":"t4","task":f"Lunch: {profile.get('preferences',{}).get('lunch_default','Paneer Sandwich')} — confirm","status":"pending","category":"health"},
            {"id":"t5","task":"Client Email Review — drafts ready","status":"pending","category":"work"},
            {"id":"t6","task":"Team Meeting — slides in SharePoint","status":"pending","category":"work"},
            {"id":"t7","task":f"Family Dinner at {profile.get('preferences',{}).get('family_restaurant','myChef')} 6 PM","status":"pending","category":"family"}
        ]
        return plan
