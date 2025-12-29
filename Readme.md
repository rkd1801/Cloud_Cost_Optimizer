# 🚀 AI-Powered Cloud Cost Optimizer

An end-to-end **LLM-driven cloud cost optimization system** that analyzes project requirements, generates realistic cloud billing data, and produces actionable cost-optimization recommendations using a **real Large Language Model (LLaMA-3.1 via Groq)**.

This project demonstrates **practical GenAI integration**, **modular system design**, **schema-driven validation**, and **cloud cost analysis** in a production-style Python application.

---

## 📌 Overview

Managing cloud infrastructure costs is challenging due to complex pricing models and evolving workloads.  
This project automates cost analysis by combining **LLMs** with **rule-based analytics** to provide structured insights and optimization recommendations.

---

## 🧠 Key Features

- 🔍 **Project Profile Extraction**  
  Converts a natural-language project description into a structured JSON profile using an LLM.

- 🧾 **Synthetic Cloud Billing Generation**  
  Generates realistic monthly cloud billing data aligned with the project profile.

- 📊 **Cost Analysis Engine**  
  Calculates total cost, service-wise breakdown, and budget variance.

- 💡 **Optimization Recommendations**  
  Provides actionable suggestions such as:
  - Reserved instances
  - Resource right-sizing
  - Database optimization
  - Storage tiering

- ✅ **JSON Schema Validation**  
  Ensures correctness and consistency of all intermediate outputs.

- 🖥️ **Menu-Driven CLI Interface**  
  Simple command-line workflow for executing the complete pipeline.

---

## 🏗️ Architecture

User Input (CLI)
│
▼
Project Description
│
▼
LLM → Project Profile (JSON)
│
▼
LLM → Cloud Billing Data (JSON Array)
│
▼
Cost Analyzer
│
▼
Cost Optimization Report (JSON)


---

## 🛠️ Tech Stack

| Component | Technology |
|---------|------------|
| Language | Python 3.10+ |
| LLM Provider | Groq |
| Model | LLaMA-3.1-8B-Instant |
| Validation | JSON Schema |
| Interface | Command Line (CLI) |
| Version Control | Git & GitHub |

---

## 📁 Project Structure

cloud_cost_optimizer/
│
├── cli/
│ └── menu.py
│
├── core/
│ ├── llm_client.py
│ ├── profile_extractor.py
│ ├── billing_generator.py
│ └── cost_analyzer.py
│
├── schemas/
│ ├── project_profile.schema.json
│ ├── mock_billing.schema.json
│ └── cost_report.schema.json
│
├── utils/
│ ├── validator.py
│ └── file_io.py
│
├── data/ # Generated outputs (ignored in Git)
├── main.py
├── requirements.txt
├── .gitignore
└── README.md


---

## ⚙️ Setup Instructions

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/<your-username>/cloud-cost-optimizer.git
cd cloud-cost-optimizer

### 2 Install Dependencies
pip install -r requirements.txt

### 3 Configure Environment Variables

Create a .env file in the project root:

GROQ_API_KEY=your_groq_api_key_here


🔐 The .env file is excluded from version control.


## ▶️ How to Run (Important)

Always run the project from the **parent directory** (e.g. Desktop):

```bash
cd path/to/Desktop
python -m cloud_cost_optimizer.main

##  HTML Report

- **What**: Generates an HTML summary of the cost optimization report.
- **How to generate**: Run the pipeline (for example `python -m cloud_cost_optimizer.main`), or use the CLI menu.
- **Where it's saved**: The HTML file is exported to your Desktop (OneDrive Desktop fallback) with the filename pattern `cloud_cost_report_<YYYYMMDD_HHMMSS>.html`.
- **Auto-open**: The report attempts to open automatically in your default browser after generation.
- **See code**: `report/export_report.py` contains the exporter logic and filename pattern.

