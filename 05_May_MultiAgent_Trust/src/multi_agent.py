import os

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# 1. A Function Called orchestrator_agent(goal)
#    That Prints The Goal And Calls research_agent()
def orchestrator_agent(goal):
    print(f"Orchestrator Agent Received The Goal: {goal}")
    research_result = research_agent(goal)
    execution_result = executor_agent(research_result)
    return execution_result


# 2. A Function Called research_agent(task)
#    That Returns A Hardcoded Research Result String
def research_agent(task):
    try:
        with open(os.path.join(ROOT_DIR, "logs", "research_data.txt"), "r", encoding="utf-8") as file:
            content = file.read()
    except (FileNotFoundError, PermissionError) as e:
        return f"Error: Could Not Read Research Data. Reason: {e}"
    except Exception as e:
        return f"Error: {e}"
    finally:
        print(f"Log Read Attempt Complete.")
    return content


# 3. A Function Called executor_agent(research)
#    That Prints What It Received And Returns "Execution Complete"
def executor_agent(research):
    print(f"Executor Agent Received The Research: {research}")
    return "Execution Complete"


if __name__ == "__main__":
    final_result = orchestrator_agent("Check System Security Status")
    print(f"Final Result: {final_result}")
