from groq import generate_response
def prompt_engineering():
    print("Welcome to AI prompt engineering tutorial")
    vague = input("Enter a vague prompt: ")
    print(generate_response(vague))

    specific = input("Now, make it more specific: ")
    print(generate_response(specific))

    context = input("Now, add context: ")
    print(generate_response(context))
    print("\n--- Reflection ---")

    print("1. How did the AI's response change when the prompt was made more specific?")

    print("2. How did the AI's response improve with the added context?")

    print("3. Which prompt produced the most relevant and tailored response? Why?")

if __name__ == "__main__":
    prompt_engineering()