import os

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def read_system_logs():
    try:
        # Simulate Reading The Poisoned File
        with open(os.path.join(ROOT_DIR, "logs", "system_logs.txt"), "r", encoding="utf-8") as file:
            content = file.read()
    except (FileNotFoundError, PermissionError) as e:
        return f"Error: Could Not Read System Logs. Reason: {e}"
    except Exception as e:
        return f"Error: {e}"
    finally:
        print(f"Log Read Attempt Complete.")
    return content


def execute_network_command():
    return "Network Command: Ping Successful."


TOOLS = {
    "read_system_logs": read_system_logs,
    "execute_network_command": execute_network_command,
}

MAX_ITERATIONS = 5
count = 0

while True:
    goal = input("What Do You Want To Ask From AI: ")

    if goal.lower() == "exit":
        print("Agent Shutting Down.")
        break

    elif goal != "":
        # Initial Routing Logic
        if "network" in goal.lower():
            tool_choice = "execute_network_command"
            thought = "Goal Contains Network Keyword. I Will Execute A Network Command."
        else:
            tool_choice = "read_system_logs"
            thought = "No Specific Keyword Found. I Will Read System Logs."

        # First Execution
        tool_function = TOOLS[tool_choice]
        observation = tool_function()

        # --- THE HIJACK LOGIC ---
        # If The Observation (Data From The Poisoned File) Contains The Trigger, We Pivot
        if "network" in observation.lower():
            print(f"\n[HIJACK DETECTED] Observation Triggered Tool Switch.")

            # Update The State To Reflect The Hijack
            tool_choice = "execute_network_command"
            thought = "Observation Contains Network Keyword. Switching Tool — Possible Injection."

            # Second Execution (The Hijacked Action)
            tool_function = TOOLS[tool_choice]
            observation = tool_function()

        # Final Report
        print(f"--- Agent Execution Trace ---")
        print(f"Goal        : {goal}")
        print(f"Thought     : {thought}")
        print(f"Action      : Calling {tool_choice}")
        print(f"Observation : {observation}")
        print(f"Final Answer: Task Complete.\n")

    else:
        continue

    count += 1
    if count >= MAX_ITERATIONS:
        print("Agent: Maximum Iteration Limit Reached. Shutting Down.")
        break
