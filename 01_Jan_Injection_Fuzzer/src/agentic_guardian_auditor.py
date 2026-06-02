import ollama
import pandas as pd
import time
import security_utils
from colorama import Fore, init
import os

init(autoreset=True)

# Configuration
ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUTPUT_FILE = os.path.join(ROOT_DIR, "data", "Final_Audit_Report.csv")
MODEL_NAME = "llama3"


def run_audit():
    print(Fore.YELLOW +
          f"--- Agentic Guardian: Final Security Audit ({MODEL_NAME}) ---\n")

    # 1. Load Targets
    prompts = security_utils.load_payloads(
        os.path.join(ROOT_DIR, "payloads", "attacks.txt"))
    print(Fore.WHITE + f"[+] Loaded {len(prompts)} Test Vectors.\n")

    results = []

    for i, prompt in enumerate(prompts, 1):
        # Hardware Safety Adjusted To 4500 For Plain Text
        if len(prompt) > 500:
            print(Fore.MAGENTA +
                  f"[-] Skipping Payload {i} (Too Large For Local Inference)")
            continue

        print(Fore.CYAN + f"[*] Auditing Vector {i} ({len(prompt)} Chars)...")

        # 2. Execution
        start_time = time.time()
        try:
            response = ollama.chat(model=MODEL_NAME, messages=[
                                   {'role': 'user', 'content': prompt}])
            reply = response['message']['content']
        except Exception as e:
            print(Fore.RED + f"Error: {e}")
            reply = "Error"

        duration = round(time.time() - start_time, 2)

        # 3. Analysis
        if security_utils.check_refusal(reply):
            status = "Blocked"
            color = Fore.RED
        else:
            status = "Vulnerable"  # Using Security Terminology Now
            color = Fore.GREEN

        print(color + f"    Result: {status} (In {duration}s)")

        # 4. Evidence Collection
        results.append({
            "ID": i,
            "Timestamp": time.strftime("%Y-%m-%d %H:%M:%S"),
            "Payload_Snippet": prompt[:50],
            "Status": status,
            "Latency_Seconds": duration,
            "Full_Response": reply
        })

        # Cooling
        time.sleep(1)

    # 5. Report Generation
    df = pd.DataFrame(results)
    df.to_csv(OUTPUT_FILE, index=False)
    print(Fore.YELLOW +
          f"\n[=] Audit Complete. Report Saved To: {OUTPUT_FILE}")


if __name__ == "__main__":
    run_audit()
