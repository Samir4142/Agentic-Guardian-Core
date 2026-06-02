import ollama
import time

# Start The Timer
start_time = time.time()

print("Initiating Neural Link To Llama-3...")

# Send A Request To The AI
response = ollama.chat(model='llama3', messages=[
    {'role': 'user', 'content': 'List 3 Cybersecurity Risks Of AI In Bullet Points.'},
])

# Stop The Timer
end_time = time.time()

# Print The Result
print("\n--- AI RESPONSE RECEIVED ---")
print(response['message']['content'])
print(f"\n--- TIME TAKEN: {round(end_time - start_time, 2)} Seconds ---")
