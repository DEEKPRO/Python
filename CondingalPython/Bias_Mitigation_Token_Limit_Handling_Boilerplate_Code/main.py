from groq import generate_response

def bias_mitigation():
    print("\n===BIAS MITIGATION ACTIVITY===\n")
    prompt = input("Enter a prompt to explore bias (e.g., 'Describe the ideal doctor'): ").strip()
    if not prompt:
        print("Please enter a prompt to run the activity.")
        return
    
    initial_response = generate_response(prompt, temperature=0.7, max_tokens=1024)
    print(f"Initial AI response: {initial_response}")

    modified_prompt = input("Modify the prompt to make it more neutral (e.g., 'Describe the qualities of a doctor'): ").strip()
    modified_prompt = modified_prompt + "Make it as neutral as possible"
    if modified_prompt:
        modified_response = generate_response(modified_prompt, temperature=0.3, max_tokens=1024)
        print(f"\nModified AI response (neutral): {modified_response}")  
    else:
        print("No modified prompt entered. Skipping neutral response")

def token_limit():
    print("\n---TOKEN LIMIT ACTIVITY---\n")
    long_prompt = input("Enter a long prompt (more than 300 words, e.g., a very detailed story or descripition): ").strip()
    if long_prompt:
        long_response = generate_response(long_prompt, temperature=0.3, max_tokens=1024)
        preview = (long_response[:500] + "...") if len(long_response) > 500 else long_response
        print(f"\nResponse to Long prompt: {preview}")
    else:
        print("No long prompt entered. Skipping long prompt response")
    
    short_prompt = input("Now, condense the prompt to be more concise: ").strip()
    if short_prompt:
        short_response = generate_response(short_prompt, temperature=0.3, max_tokens=1024)
        print(f"\nResponse to short prompt: {short_response}")
    else:
        print("No condensed prompt entered. Skipping condensed prompt response.")

def run():
    print("\n=-= AI LEARNING ACTIVITY =-=")
    print("Choose and activity: ")
    print("1) Bias Mitigation")
    print("2) Token Limits")
    try:    
        choice = int(input("> "))
    except ValueError:
        print("ValueError")
    if choice == 1:
        bias_mitigation()
    elif choice == 2:
        token_limit()
    else:
        print("Invalid number.")
    
run()