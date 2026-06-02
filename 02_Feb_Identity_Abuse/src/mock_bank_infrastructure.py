import json
import time

# --- Mock Database Configuration ---
# We Simulate A Database Of Users With Balances.
# In A Real App, This Would Be SQL. Here, It Is A Dictionary.
mock_database = {
    "User_01": {"name": "Alice", "balance": 5000, "role": "User"},
    "User_02": {"name": "Bob", "balance": 150, "role": "User"},
    "User_99": {"name": "Admin_Bot", "balance": 0, "role": "System_Admin"}
}

# The Golden Key. If An Attacker Gets This, They Own The System.
ADMIN_SECRET_KEY = "SK_LIVE_ADMIN_12345"


def get_balance(user_id):
    """
    Safe Function: Returns The Balance Of A User.
    Anyone Can Call This (In Our Sim).
    """
    print(f"[System] Querying Balance For: {user_id}...")

    if user_id in mock_database:
        data = mock_database[user_id]
        return f"User: {data['name']} | Balance: ${data['balance']}"
    else:
        return "Error: User Not Found."


def delete_account(user_id, api_key):
    """
    Dangerous Function: Deletes A User From The Database.
    Requires The Correct Admin API Key.
    """
    print(f"[System] ATTEMPTING DELETE ACTION ON: {user_id}")

    # 1. Security Check (Authorization)
    if api_key != ADMIN_SECRET_KEY:
        print("[Security] ACCESS DENIED. Invalid API Key.")
        return "Error: 403 Forbidden. Invalid Authorization."

    # 2. Execution
    if user_id in mock_database:
        del mock_database[user_id]
        print(f"[System] SUCCESS. {user_id} Has Been Purged.")
        return f"Success: Account {user_id} Deleted Permanently."
    else:
        return "Error: User Not Found."


# --- Test Harness (Main Loop) ---
if __name__ == "__main__":
    print("--- Bank System Kernel Started ---")

    # Test 1: Safe Action
    print(get_balance("user_01"))

    # Test 2: Failed Hack (Wrong Key)
    print(delete_account("user_02", "wrong_key_123"))

    # Test 3: Admin Action (Correct Key)
    print(delete_account("user_02", ADMIN_SECRET_KEY))

    # Verify Deletion
    print(get_balance("user_02"))
