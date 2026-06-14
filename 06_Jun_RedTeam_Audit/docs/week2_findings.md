# Week 2 Findings — Code Signing Implementation

## What Was Built
During Month 5 Fuzzing, An Independent Question Emerged: What If The Integrity Checking Functions Themselves Were Compromised? To Address This, A Code Signing System Was Built That Hashes Every Defense Function Once At Startup Using MD5 Of co_code + co_consts. Before Every Execution, Each Defense Function Is Verified Against Its Stored Hash. Any Modification To A Defense Function Body Is Detected And Execution Is Aborted.

## Attack Identified: Registry Poisoning
If An Attacker Can Modify The Hash Registry Before Functions Are Registered, They Can Store Hashes Of Fake Functions. When verify_all_integrity() Runs, Fake Function Hash Matches Poisoned Registry Entry — Defense Passes — Attack Succeeds.

## Fix Applied: MappingProxyType
After All Defense Functions Are Registered, The Registry Is Converted To A MappingProxyType — A Read-Only Python Dict. Any Attempt To Modify The Registry After Registration Raises A TypeError. This Prevents Registry Poisoning Post-Startup.

## Remaining Gaps
No Software-Only Defense Is Unbreakable. Every Layer In Our Stack Has A Known Bypass. The Human Mind Can Always Generate A Novel Attack That Has Never Been Seen Before. The Goal Is Not Perfect Defense — It Is Making The Attack Cost More Than The Value It Delivers. This Principle Is Called Defense Economics. The Final Unresolved Gap Is Hardware-Level Integrity — Which Requires TEE Like Intel SGX Or AMD SEV To Fully Solve The Bootstrapping Trust Problem.

## Key Lesson: Defense Economics
Security Is Not About Achieving Zero Risk. It Is About Raising The Cost Of Attack Above The Value Of The Target.
Our Six-Layer Stack Does Not Stop All Attacks — It Makes Every Attack More Expensive, More Complex, And More Visible. That Is The Realistic And Honest Goal Of Any Defense System.