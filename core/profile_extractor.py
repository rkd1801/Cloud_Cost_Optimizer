import json
import os
from cloud_cost_optimizer.core.llm_client import call_llm
from cloud_cost_optimizer.utils.validator import validate_json
from cloud_cost_optimizer.utils.file_io import write_json

def generate_project_profile(description: str):
    prompt = f"""
Extract a structured JSON project profile.

Rules:
- Output ONLY valid JSON
- No explanation text
- Fields:
  name, budget_inr_per_month, description,
  tech_stack (object), non_functional_requirements (array)

Input:
{description}
"""
    response = call_llm(prompt)
    profile = json.loads(response)

    validate_json(profile, "project_profile.schema.json")
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    DATA_DIR = os.path.join(BASE_DIR, "data")
    write_json(os.path.join(DATA_DIR, "project_profile.json"), profile)

