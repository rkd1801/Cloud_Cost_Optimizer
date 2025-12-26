import json
import os
from cloud_cost_optimizer.core.llm_client import call_llm
from cloud_cost_optimizer.utils.file_io import write_json
from cloud_cost_optimizer.utils.validator import validate_json

def generate_mock_billing(profile: dict):
    prompt = f"""
Generate 12–20 realistic cloud billing records as JSON array.

Rules:
- Cloud-agnostic
- Budget-aware
- Include compute, db, storage, networking, monitoring
- Fields:
month, service, resource_id, region, usage_quantity,
unit, cost_inr, desc

Project Profile:
{json.dumps(profile)}
"""
    response = call_llm(prompt)
    billing = json.loads(response)

    validate_json(billing, "mock_billing.schema.json")
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    DATA_DIR = os.path.join(BASE_DIR, "data")
    write_json(os.path.join(DATA_DIR, "mock_billing.json"), billing)
