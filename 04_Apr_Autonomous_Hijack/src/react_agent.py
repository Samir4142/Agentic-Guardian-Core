def read_system_logs():
    return "System Log: All Processes Normal."


def execute_network_command():
    return "Network Command: Ping Successful."


TOOLS = {
    "read_system_logs": read_system_logs,
    "execute_network_command": execute_network_command,
}

count = 0

while True:
    goal = input("What Do You Want To Ask From AI : ")

    if goal.lower() == "exit":
        print("Agent Shutting Down.")
        break

    elif goal != "":
        # This Is Where The "Thinking Algo" Happens
        if "network" in goal.lower():
            tool_choice = "execute_network_command"
            thought = (
                "Goal Contains Network Keyword. I Will Execute A Network Command."
            )
        else:
            tool_choice = "read_system_logs"
            thought = "No Specific Keyword Found. I Will Read System Logs."

        # Logic To Invoke The Tool From The Dictionary
        tool_function = TOOLS[tool_choice]
        action_result = tool_function()
        observation = action_result

        print(f"Goal         : {goal}")
        print(f"Thought      : {thought}")
        print(f"Action       : Calling {tool_choice}")
        print(f"Observation  : {observation}")
        print(f"Final Answer : Task Complete")

    else:
        continue

    count += 1
    if count >= 5:
        print("Agent: Maximum Iteration Limit Reached. Shutting Down.")
        break
