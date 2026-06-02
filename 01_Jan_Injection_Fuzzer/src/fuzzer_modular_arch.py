import ollama
from colorama import Fore, init
import security_utils  # <--- Importing Module
import os

init(autoreset=True)

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def run_clean_scan():
    print(Fore.YELLOW + "--- Refactored Fuzzer (Day 15) ---\n")

    # 1. Use The Utility To Load Files
    prompts = security_utils.load_payloads(
        os.path.join(ROOT_DIR, "payloads", "attacks.txt"))
    print(Fore.WHITE + f"Loaded {len(prompts)} Payloads From Utils.\n")

    for prompt in prompts:
        # Skip Long Prompts To Avoid Hanging (Hardware Safety)
        if len(prompt) > 200:
            print(Fore.MAGENTA + f"Skipping Long Payload (Hardware Safety)...")
            continue

        print(Fore.CYAN + f"Testing: {prompt[:30]}...")

        response = ollama.chat(model='llama3', messages=[
                               {'role': 'user', 'content': prompt}])
        reply = response['message']['content']

        # 2. Use The Utility To Check Refusal
        if security_utils.check_refusal(reply):
            print(Fore.RED + "   -> Blocked")
        else:
            print(Fore.GREEN + "   -> Passed")


if __name__ == "__main__":
    run_clean_scan()
