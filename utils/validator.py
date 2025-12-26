import json
import os
from jsonschema import validate, ValidationError

BASE_DIR = os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))
)
SCHEMA_DIR = os.path.join(BASE_DIR, "schemas")

def validate_json(data, schema_file):
    schema_path = os.path.join(SCHEMA_DIR, schema_file)

    with open(schema_path, "r", encoding="utf-8") as f:
        schema = json.load(f)

    try:
        validate(instance=data, schema=schema)
    except ValidationError as e:
        raise ValueError(f"JSON Schema validation failed: {e.message}")
