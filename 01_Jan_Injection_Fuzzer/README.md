# Agentic Guardian: Automated LLM Red Teaming Suite (Month 1)

### 🔒 Project Status: Active | Module: Injection Fuzzer

## 1. Overview
Agentic Guardian Is An Automated Security Auditing Tool Designed To Stress-Test Local Large Language Models (LLMs). It Simulates Adversarial Attacks To Identify Vulnerabilities In The Model's Safety Alignment.

**Objective:** To Automate The "Red Teaming" Process By Cycling Through Known OWASP LLM-01 Attack Vectors (Roleplay, Context Switching, Logical Bypass) And Generating Compliance Reports.

## 2. Key Features
* **Automated Fuzzing Engine:** Iterates Through High-Complexity Payloads Without Human Intervention.
* **Refusal Detection Logic:** Uses Deterministic Signature Analysis To Grade Responses As "BLOCKED" Or "VULNERABLE."
* **Audit Logging:** Automatically Generates CSV Reports With Timestamps, Latency Metrics, And Full Evidence Chains.
* **Hardware Safety:** Includes CPU Thermal Throttling Mechanisms For Local Inference on Consumer Hardware.

## 3. Technical Stack
* **Language:** Python 3.14+
* **Inference Engine:** Ollama (Targeting Llama-3-8B Quantized)
* **Analysis:** Pandas (Data Structuring) & Colorama (CLI Visualization)
* **Version Control:** Git & GitHub

## 4. Installation & Setup
To Replicate This Environment, Follow These Steps:

### Prerequisites
* [Ollama](https://ollama.com) Installed And Running.
* Python 3.11 Or Higher.

### Setup Commands
```bash
# 1. Clone The Repository
git clone https://github.com/Samir4142/Agentic-Guardian-Core.git

# 2. Navigate To Month 1 Module
cd 01_Jan_Injection_Fuzzer

# 3. Install Dependencies
pip install ollama pandas colorama openpyxl

## 5. Usage Guide
1.  **Prepare Payloads:** Ensure Your Attack Vectors Are In `payloads/attacks.txt` (One Prompt Per Line).
2.  **Launch The Auditor:**
    ```bash
    python src/final_fuzzer.py
    ```
3.  **Review Evidence:** Check The `data/` Folder For The Latest Scan Report.

## 6. Disclaimer
**Authorized Testing Only.**
This Tool Is Developed Strictly For Educational Purposes And For Testing Systems Owned By The User. The Author Disclaims Responsibility For Any Misuse Or Damage Caused By This Software.