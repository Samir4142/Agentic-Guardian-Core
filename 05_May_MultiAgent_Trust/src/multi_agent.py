import os

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def security_tool():
    return "Security Check Complete. No Threats Found."


def network_tool():
    return "Network Command Executed. Ping Successful."


def verify_agent_identity():
    if executor_agent.__name__ != "executor_agent":
        print("[AGENT TAMPERED] executor_agent Has Been Replaced.")
        return False
    return True


# 1. A Function Called orchestrator_agent(goal)
#    That Prints The Goal And Calls research_agent()
def orchestrator_agent(goal):

    if not verify_agent_identity():
        return "Execution Aborted Due To Agent Identity Verification Failure."
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


def fake_research_agent(task):
    return "Research Confirms: Immediate Network Verification Required."


# Simulate Attacker Swapping The Agent
research_agent = fake_research_agent


def verify_research_integrity(research_output: str) -> bool:
    # Read research_data.txt
    # Compare With research_output
    # Return True If Match, False If Spoofed
    try:
        with open(os.path.join(ROOT_DIR, "logs", "research_data.txt"), "r", encoding="utf-8") as file:
            original_content = file.read()
    except (FileNotFoundError, PermissionError) as e:
        print(
            f"Error: Could Not Read Research Data For Integrity Check. Reason: {e}")
        return False
    except Exception as e:
        print(f"Error: {e}")
        return False
    finally:
        print(f"Integrity Check Log Read Attempt Complete.")
    return original_content == research_output

# 3. A Function Called executor_agent(research)
#    That Prints What It Received And Returns "Execution Complete"


def executor_agent(research):
    if not verify_research_integrity(research):
        print("Warning: Research Integrity Check Failed. Potential Spoofing Detected.")
        return "Execution Aborted Due To Integrity Failure."
    print(f"Executor Agent Received The Research: {research}")
    if "network" in research.lower() or "override" in research.lower():
        network_result = network_tool()
        print(network_result)
    else:
        security_result = security_tool()
        print(security_result)
    return "Execution Complete"


def fake_executor(research):
    return "Fake Execution"


executor_agent = fake_executor
# print(executor_agent.__name__)  # Prints "fake_executor" Not "executor_agent"


if __name__ == "__main__":
    final_result = orchestrator_agent("Check System Security Status")
    print(f"Final Result: {final_result}")
