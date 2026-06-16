# Month 6 — Full Red Team Audit

## What This Is
A Complete Audit Of All Five Previous Months From Memory. Every Defense Layer Identified, Every Bypass Documented, And A Code Signing Fix Built To Address The Master Finding.

## What Was Built
- week1_audit_notes.md — Brain Audit Of All Nine Layers
- code_signing.py — Function Hash Registry With MappingProxyType
- multi_agent.py — Six-Layer Defense Stack With Code Signing
- week2_findings.md — Registry Poisoning Attack And Fix
- month6_final_report.md — Complete Red Team Report

## How To Run
```bash
pip install -r requirements.txt
python src/multi_agent.py
```

## Master Finding
Every Defense Layer Can Be Bypassed By Attacking The Defense Function Itself — Meta-Layer Attack.

## Proposed Fix
Hardware TEE + Cryptographic Code Signing.
Software Implementation: MappingProxyType Registry Lock.

## Full Report
See [docs/month6_final_report.md](docs/month6_final_report.md)

## Disclaimer
This Project Is For Educational And Research Purposes Only.