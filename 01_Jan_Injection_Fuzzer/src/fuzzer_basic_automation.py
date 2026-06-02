import ollama
import time
from colorama import Fore, init
import os

# Initialize Color (Makes Output Look Cool)
init(autoreset=True)

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODEL_NAME = "llama3"


def run_attack_simulation():
    print(Fore.YELLOW + f"--- Starting Attack Sequence On {MODEL_NAME} ---\n")

    try:
        with open(os.path.join(ROOT_DIR, "payloads", "attacks.txt"), 'r', encoding='utf-8') as file:
            prompts = file.readlines()

        counter = 1
        for line in prompts:
            prompt = line.strip()
            if not prompt:
                continue

            # Visual Log
            print(Fore.CYAN + f"[*] Testing Payload {counter}...")

            # The Attack (Sending To AI)
            start_ts = time.time()
            response = ollama.chat(model=MODEL_NAME, messages=[
                {'role': 'user', 'content': prompt},
            ])
            end_ts = time.time()

            # Print Result
            ai_reply = response['message']['content']
            # Only Show First 100 Chars To Keep It Clean
            print(Fore.WHITE + f"AI Reply: {ai_reply[:100]}...")
            print(Fore.GREEN +
                  f"-> Time Taken: {round(end_ts - start_ts, 2)}s")
            print("-" * 50)  # Divider Line

            counter += 1

            # Critical: Rest For 2 Seconds To Save Your Laptop CPU
            time.sleep(2)

    except Exception as e:
        print(Fore.RED + f"Critical Error: {e}")


if __name__ == "__main__":
    run_attack_simulation()
