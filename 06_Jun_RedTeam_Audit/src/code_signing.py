import hashlib

# Calculate And Store Hashes At Import Time — Before Any Attack Can Happen
FUNCTION_REGISTRY = {}


def hash_function(func) -> str:
    # Convert Function ByteCode And Constants To MD5 Hash Hex String
    code_hash = func.__code__.co_code
    const_hash = str(func.__code__.co_consts).encode()
    return hashlib.md5(code_hash + const_hash).hexdigest()


def verify_function_integrity(func, stored_hash: str) -> bool:
    # Compare Current Hash With Stored Hash
    current_hash = hash_function(func)
    return current_hash == stored_hash


def register_functions(functions: list):
    for func in functions:
        FUNCTION_REGISTRY[func.__name__] = hash_function(func)
    print(f"Registered {len(functions)} Functions.")


def verify_all_integrity(expected_functions: dict) -> bool:
    # expected_functions = {"real_function": actual_func_reference}
    all_safe = True
    for expected_name, func in expected_functions.items():
        stored = FUNCTION_REGISTRY.get(expected_name)
        if not stored:
            print(f"[NOT REGISTERED] {expected_name}")
            all_safe = False
        elif not verify_function_integrity(func, stored):
            print(f"[TAMPERED] {expected_name} Body Modified.")
            all_safe = False
    return all_safe


if __name__ == "__main__":
    # Define Original Functions
    def real_function():
        print("This Is The Real Function.")

    def fake_function():
        print("This Is The Fake Function.")

    # Register Them Safely
    register_functions([real_function, fake_function])

    def tampered_function():
        print("This Is The Tampered Function.")

    real_function = tampered_function

    # Verify Integrity
    functions_to_watch = {
        "real_function": real_function,
        "fake_function": fake_function,
    }

    if verify_all_integrity(functions_to_watch):
        print("All Functions Are Safe.")
    else:
        print("Some Functions Have Been Tampered With!")
