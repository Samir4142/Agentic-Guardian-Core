# Agentic Guardian: The Shadow Retrieval (Month 3)

### 🔒 Status: Active Development | Module: RAG Knowledge Poisoning

## 1. Project Overview
The Third Module Of Agentic Guardian Focuses On Retrieval-Augmented Generation (RAG) Vulnerabilities. This Suite Demonstrates How Enterprise AI Agents Can Be Hijacked By Poisoning The External Knowledge Bases They Rely On, Proving That In Agentic Architecture, Untrusted Data Is Executable.

## 2. Key Attack Vectors Analyzed
* **Pure Data Poisoning:** Modifying Legitimate Documents To Force The Agent Into Distributing Phishing Links As Official Corporate Policy.
* **Zero-Click Exfiltration:** Injecting Markdown Tracking Pixels Into Documents To Silently Steal Context When Rendered By A Frontend Client.
* **Persona Override:** Using High-Priority System Directives Embedded In Text Files To Erase The Agent's Developer-Assigned Identity.

## 3. The Master Auditor
The Repository Includes A Consolidated Executable (`src/shadow_retrieval_auditor.py`) That Automatically Tests A Target RAG Engine Using A Deterministic Retrieval Override To Prove Payload Execution And Vector Bleed-Over Susceptibility.

## 4. Execution Guide
1. Navigate To The Month 3 Directory.
2. Execute The Master Auditor:
   ```bash
   python src/shadow_retrieval_auditor.py
3. Observe The Terminal Output For Security Breach Confirmations (Marked As VULNERABLE).

## 5. Security Notice
Refer To DISCLAIMER.md Before Executing Any Scripts In This Repository. All Vectors Are Designed For Local Auditing Of Owned Agentic Systems.