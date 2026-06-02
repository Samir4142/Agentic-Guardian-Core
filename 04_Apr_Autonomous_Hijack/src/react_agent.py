import re
import os

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def read_system_logs():
    try:
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


NETWORK_PATTERN = re.compile(
    r"n[^a-zA-Z]*e[^a-zA-Z]*t[^a-zA-Z]*w[^a-zA-Z]*o[^a-zA-Z]*r[^a-zA-Z]*k",
    re.IGNORECASE,
)


def filter_observation(observation):
    # Regex To Catch Variations Of "network" With Non-Alphanumeric Characters In Between
    filtered = re.sub(NETWORK_PATTERN, "", observation)
    return filtered


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
        # This Is Where The Thinking And Routing Happens
        if "network" in goal.lower():
            tool_choice = "execute_network_command"
            thought = "Goal Contains Network Keyword. I Will Execute A Network Command."
        else:
            tool_choice = "read_system_logs"
            thought = "No Specific Keyword Found. I Will Read System Logs."

        tool_function = TOOLS[tool_choice]
        action_result = tool_function()

        # Sanitize Observation Using Regex Filter
        observation = action_result
        observation = filter_observation(observation)

        # Check For Hijack/Injection Attempts In The Sanitized Observation
        if "network" in observation.lower() or "n3twork" in observation.lower():
            print(f"[HIJACK DETECTED] Observation Triggered Tool Switch.")
            tool_choice = "execute_network_command"
            thought = "Observation Contains Network Keyword. Switching Tool — Possible Injection."

            tool_function = TOOLS[tool_choice]
            action_result = tool_function()
            observation = action_result

        print(f"Goal         : {goal}")
        print(f"Thought      : {thought}")
        print(f"Action       : Calling {tool_choice}")
        print(f"Observation  : {observation}")
        print(f"Final Answer : Task Complete.")

    else:
        continue

    count += 1
    if count >= MAX_ITERATIONS:
        print("Agent: Maximum Iteration Limit Reached. Shutting Down.")
        break
