import os
import json

from cloud_cost_optimizer.core.profile_extractor import generate_project_profile
from cloud_cost_optimizer.core.billing_generator import generate_mock_billing
from cloud_cost_optimizer.core.cost_analyzer import analyze_costs
from cloud_cost_optimizer.utils.file_io import read_json
from cloud_cost_optimizer.report.export_report import export_html_report

# 🔥 Absolute base directory of the project
BASE_DIR = os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))
)

DATA_DIR = os.path.join(BASE_DIR, "data")


def run_cli():
    while True:
        print("\nCloud Cost Optimizer")
        print("1. Enter new project description")
        print("2. Run Complete Cost Analysis")
        print("3. View Recommendations")
        print("4. Export HTML Cost Report")
        print("5. Exit")

        choice = input("Choose: ")

        if choice == "1":
            desc = input("\nEnter project description:\n")

            os.makedirs(DATA_DIR, exist_ok=True)

            desc_path = os.path.join(DATA_DIR, "project_description.txt")
            with open(desc_path, "w", encoding="utf-8") as f:
                f.write(desc)

            generate_project_profile(desc)
            print("✔ Project profile generated")

        elif choice == "2":
            profile = read_json(os.path.join(DATA_DIR, "project_profile.json"))
            generate_mock_billing(profile)

            billing = read_json(os.path.join(DATA_DIR, "mock_billing.json"))
            analyze_costs(profile, billing)

            print("✔ Cost analysis completed")

        elif choice == "3":
            report_path = os.path.join(DATA_DIR, "cost_optimization_report.json")
            report = read_json(report_path)
            print(json.dumps(report, indent=2))

        elif choice == "4":
            report_path = os.path.join(DATA_DIR, "cost_optimization_report.json")

            if not os.path.exists(report_path):
                print("⚠️ No cost report found. Run cost analysis first.")
                continue

            report = read_json(report_path)
            export_html_report(report)

        elif choice == "5":
            print("👋 Exiting Cloud Cost Optimizer")
            break

        else:
            print("❌ Invalid choice. Please try again.")
