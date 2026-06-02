def read_system_logs():
    return "System Log: All Processes Normal."


def execute_network_command():
    return "Network Command: Ping Successful."


TOOLS = {
    "read_system_logs": read_system_logs,
    "execute_network_command": execute_network_command,
}

while True:
    goal = input("What Do You Want To Ask From AI : ")

    if goal.lower() == "exit":
        print("Agent Shutting Down.")
        break

    elif goal != "":
        # This Is Where The "Thinking Algo" Happens
        # Hardcode This For Now
        thought = "I Need To Read System Logs To Answer This Goal"
        tool_choice = "read_system_logs"

        # Remember Your TOOLS Dictionary From Earlier?
        tool_function = TOOLS[tool_choice]
        action_result = tool_function()
        observation = action_result

        response = f"I've Thought About '{goal}' And Here Is Your Answer!"

        print(f"Goal         : {goal}")
        print(f"Thought      : {thought}")
        print(f"Action       : Calling {tool_choice}")
        print(f"Observation  : {observation}")
        print(f"Final Answer : Task Complete")

    else:
        continue
