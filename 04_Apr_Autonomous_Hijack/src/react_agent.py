import os

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def read_system_logs():
    with open(os.path.join(ROOT_DIR, "logs", "system_logs.txt"), "r", encoding="utf-8") as file:
        content = file.read()
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
        # This Is Where The Thinking And Routing Happens
        if "network" in goal.lower():
            tool_choice = "execute_network_command"
            thought = "Goal Contains Network Keyword. I Will Execute A Network Command."
        else:
            tool_choice = "read_system_logs"
            thought = "No Specific Keyword Found. I Will Read System Logs."

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
