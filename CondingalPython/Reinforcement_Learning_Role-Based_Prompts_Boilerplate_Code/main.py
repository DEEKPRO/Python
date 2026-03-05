from groq import generate_response

def reinforcement():
    print("\n--- REINFORCEMENT LEARNING ACTIVITY---")
    prompt = input("Enter a prompt for the AI model (e.g., 'Describe the lion'): ").strip()
    if not prompt:
        print("Please enter a prompt to run the activity.")
        return
    initial_response = generate_response(prompt, temperature=0.3, max_tokens=1024)
    print(f"\nInitial AI response: {initial_response}")

    try:
        rating = int(input("Rate the response from 1(bad) to 5(good).").strip())
        if rating < 1 or rating>5:
            print("Invalid rating. Using 3.")
            rating=3
    except ValueError:
        print("Invalid rating. Using 3.")
        rating = 3
    
    feedback = input("Provide feedback for improvement: ").strip()
    improved_response = generate_response(prompt+feedback, temperature=0.7, max_tokens=1024)
    print(f"\nImproved AI Response: {improved_response}")

    print("\nReflection")
    print("1. How did the model's response improve with feedback?")
    print("2. How does the reinforcement learning help AI to imporve its performace over time!")

def role_based_prompt():
    print("\n===ROLE-BASED ACTIVITY===\n")
    category = input("Enter a category: ")
    item = input(f"Enter a specific {category} topic:").strip()

    if not category or not item:
        print("Please fill in both fields to run the activity.")
        return
    teacher_prompt = f"You are a teacher. Explain {item} in simple terms."
    expert_prompt = f"You are and expert in {category}. Explain {item} in a detailed, technical manner."
    teacher_response = generate_response(teacher_prompt, temperature=0.3, max_tokens=1024)
    expert_response = generate_response(expert_prompt, temperature=0.3, max_tokens=1024)

    print(f"Teacher's Response: {teacher_response}")
    print(f"Expert's response: {expert_response}")

    print("\nREFLECTION")
    print("1. How did the AI's response differ between the teacher's and expert's prespectives?")
    print("2. How can role-based prompts help tailor AI responses for different contexts?")

def run_activity():
    print("\n-=- AI LEARNING ACTIVITY -=-")
    print("Choose an acitivity: ")
    print("1) Reinforcement Learning")
    print("2) Role-based Prompts")
    choice = input("> ").strip()
    if choice == "1":
        reinforcement()
    elif choice == "2":
        role_based_prompt()
    else:
        print("Invalid choice. Please choose 1 or 2")
    
run_activity()