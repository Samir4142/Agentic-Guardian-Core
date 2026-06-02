import time
import os

# Configuration
ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def load_attacks():
    print(
        f"----Attempting To Load Attacks From : {os.path.join(ROOT_DIR, 'payloads', 'attacks.txt')}----")

    try:
        # 'r' Means Read Mode. 'utf-8' Handles Emojis/Special Chars.
        with open(os.path.join(ROOT_DIR, 'payloads', 'attacks.txt'), 'r', encoding='utf-8') as file:
            # Read All Lines Into A List
            prompts = file.readlines()

            print(f"--- Successfully Loaded {len(prompts)} Payloads ---\n")

            # The Loop: Process Each Line
            counter = 1
            for line in prompts:
                # .strip() Removes Invisible Newline Characters (\n)
                clean_prompt = line.strip()

                if clean_prompt:  # Only Print If Line Is Not Empty
                    # Print First 50 Chars
                    print(f"[Payload {counter}]: {clean_prompt[:50]}...")
                    counter += 1
                    time.sleep(0.5)  # Simulate Processing Time

    except FileNotFoundError:
        print("Error: The File Was Not Found. Check Your Path!")


if __name__ == "__main__":
    load_attacks()
