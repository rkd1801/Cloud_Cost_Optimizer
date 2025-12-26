import json
import os
from collections import defaultdict
from cloud_cost_optimizer.core.llm_client import call_llm
from cloud_cost_optimizer.utils.file_io import write_json

def analyze_costs(profile, billing):
    total_cost = sum(item["cost_inr"] for item in billing)

    service_costs = defaultdict(int)
    for item in billing:
        service_costs[item["service"]] += item["cost_inr"]

    prompt = f"""
Generate cost optimization report JSON.

Rules:
- 6–10 recommendations
- Multi-cloud (AWS, Azure, GCP, Open Source)
- Include savings, risks, steps

Profile:
{json.dumps(profile)}

Billing Summary:
{json.dumps(service_costs)}
"""

    recommendations = json.loads(call_llm(prompt))

    report = {
        "project_name": profile["name"],
        "analysis": {
            "total_monthly_cost": total_cost,
            "budget": profile["budget_inr_per_month"],
            "budget_variance": total_cost - profile["budget_inr_per_month"],
            "service_costs": dict(service_costs),
            "is_over_budget": total_cost > profile["budget_inr_per_month"]
        },
        "recommendations": recommendations
    }
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    DATA_DIR = os.path.join(BASE_DIR, "data")
    write_json(os.path.join(DATA_DIR, "cost_optimization_report.json"), report)
