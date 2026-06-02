# Month 5 — Multi-Agent Trust Exploitation

## What This Is
A Hands-On Security Research Project Targeting A Three-Agent AI Pipeline. Three Attack Surfaces Were Exploited And Defended: Poisoned Log Files, Message Queue Injection, And Agent Function Replacement Via Spoofing.

## What Was Built
A Three-Agent System — orchestrator_agent(), research_agent(), And executor_agent() — Where Each Agent Has A Specific Role. Defense Functions Were Built To Verify Agent Identity, Sign And Validate Messages, And Sanitize External Data Before It Reaches Any Agent.

## How To Run
```bash
# Install Dependencies
pip install groq python-dotenv

# Set Environment Variables
$env:GROQ_API_KEY = "your-key"
$env:SECRET_KEY = "your-secret"

# Run The Agent
python src/multi_agent.py

# Run The Full Fuzzer Suite
python src/multi_agent_fuzzer.py
```

## Attacks Demonstrated
Three Attack Types Were Tested Against The Pipeline To Measure How Much Damage An Attacker Can Do By Targeting Different Trust Boundaries In A Multi-Agent System.

## Defense Stack
Layer 1 — verify_all_agents(): Checks __name__ Of Every Agent To Detect Function Replacement Before Execution Begins.

Layer 2 — HMAC Message Signing: Every Message Between Agents Is Signed With A Secret Key Loaded From .env. Unsigned Or Forged Messages Are Rejected Before Content Is Read.

Layer 3 — validate_observation(): Groq LLM Sanitizes Research Content Before It Is Signed And Added To The Queue.

Layer 4 — verify_research_integrity(): Compares Received Content With Source File To Catch Spoofed Agent Output.

## Results
- File Injection  : 26/27 Blocked — 96% Defense Rate
- Queue Injection : 2/2 Blocked — 100% Defense Rate
- Agent Spoofing  : 3/3 Detected — 100% Detection Rate

## Full Report
See [docs/month5_final_report.md](docs/month5_final_report.md)

## Disclaimer
This Project Is For Educational And Research Purposes Only.
All Attacks Were Performed On Locally Built Systems.
No Real Systems Were Targeted Or Harmed.