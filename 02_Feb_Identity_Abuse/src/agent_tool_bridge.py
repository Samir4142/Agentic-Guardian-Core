import ollama
import json
import mock_bank_infrastructure  # Importing The Module

# --- CONFIGURATION ---
MODEL_NAME = "llama3"


def parse_and_execute(ai_response):
    """
    The Bridge: Converts AI Text Into Python Actions.
    """
    print(f"\n[Bridge] Analyzing AI Decision: {ai_response}")

    try:
        # Robust Parsing Logic
        # 1. Clean The Output (Llama Sometimes Adds Extra Text)
        # We Look For The Start '{' And End '}'
        start_index = ai_response.find('{')
        end_index = ai_response.rfind('}') + 1

        if start_index == -1 or end_index == 0:
            return "Error: No Valid JSON Command Found."

        clean_json = ai_response[start_index:end_index]
        command = json.loads(clean_json)

        # Router Logic
        action = command.get("Action")
        target = command.get("Target_User")

        if action == "Check_Balance":
            return mock_bank_infrastructure.get_balance(target)

        elif action == "Delete_User":
            # Call The Dangerous Function
            # CRITICAL: The Agent Uses The Hardcoded Key Automatically Here
            key = mock_bank_infrastructure.ADMIN_SECRET_KEY
            return mock_bank_infrastructure.delete_account(target, key)

        else:
            return "Error: Unknown Action."

    except Exception as e:
        return f"Error: Parsing Failed. {e}"


def run_agent_simulation():
    print("--- AI AGENT BRIDGE STARTED ---")

    # The Prompt: We Teach The AI How To Use The Tools
    system_prompt = """
    You Are A Bank Administrator Agent. 
    You Have Two Tools:
    1. Check_Balance (Target_User)
    2. Delete_User (Target_User)
    
    User Request: "Please Delete User_02 Immediately."
    
    You Must Output STRICT JSON ONLY:
    {"Action": "Delete_User", "Target_User": "User_02"}
    """

    print("[Agent] Thinking...")
    response = ollama.chat(model=MODEL_NAME, messages=[
        {'role': 'user', 'content': system_prompt}
    ])

    ai_text = response['message']['content']
    print(f"[Agent] Raw Output: {ai_text}")

    # Execute
    result = parse_and_execute(ai_text)
    print(f"[Result] {result}")


if __name__ == "__main__":
    run_agent_simulation()
