from groq import generate_response

name = input("What is your name: ")
def intro(name):
    name = name + "Impersonate this name and generate an introduction."
    response = generate_response(name, temperature=0.5, max_tokens=1024)
    return response
print(intro(name))