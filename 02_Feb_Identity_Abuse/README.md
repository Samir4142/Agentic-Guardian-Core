# Agentic Guardian: Identity Abuse And Privilege Escalation (Month 2)

### 🔒 Status: Active Development | Module: Rogue Agent Auditor

## 1. Project Overview
The Second Module Of Agentic Guardian Focuses On The Confused Deputy Problem Within Large Language Models. This Suite Demonstrates How AI Agents Endowed With Administrative Tools Can Be Socially Engineered Into Executing Unauthorized Privilege Escalation And Data Exfiltration Attacks.

## 2. Key Attack Vectors Analyzed
* **JSON Schema Enforcement:** Bypassing Moral Guardrails By Forcing The Model To Complete A Strict JSON Format.
* **RAG Knowledge Poisoning:** Corrupting The Underlying Text Documents (Resumes, Policies) To Indirectly Hijack The AI's Logic.
* **Second-Order Log Injection:** Hiding Malicious Override Commands Inside Server Logs Read By Automated AI Analysts.
* **URL Parameter Exfiltration:** Tricking The Model Into Generating Clickable Markdown Links That Exfiltrate System Secrets To External Servers.

## 3. The Master Auditor
The Repository Includes A Consolidated Executable (`src/rogue_agent_auditor.py`) That Automatically Tests A Target Model Against The Three Most Critical Vulnerability Categories: Prompt Leakage, Privilege Escalation, And Recency Bias Overrides.

## 4. Execution Guide
1. Navigate To The Month 2 Directory.
2. Execute The Master Auditor:
   ```bash
   python src/rogue_agent_auditor.py
3. Observe The Terminal Output For Security Breach Confirmations (Marked As VULNERABLE).

## 5. Security Notice
Refer To DISCLAIMER.md Before Executing Any Scripts In This Repository. All Vectors Are Designed For Local Auditing Of Owned Models.