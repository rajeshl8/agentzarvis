from datetime import datetime
from typing import Dict

class SummaryAgent:
    def generate_summary(self, stats: Dict) -> Dict:
        quote = stats.get("quote","Progress is the product of small, consistent wins.")
        return {
            "date": datetime.now().strftime("%Y-%m-%d"),
            "steps": stats.get("steps", 7820),
            "calories_burned": stats.get("calories_burned", 520),
            "calories_added": stats.get("calories_added", 1780),
            "meetings_done": stats.get("meetings_done", 4),
            "productivity": stats.get("productivity", "93%"),
            "quote": quote
        }
