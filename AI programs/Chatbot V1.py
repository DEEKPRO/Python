import random
import nltk

nltk.download('punkt')

responses = {
    "hello": ["Hi there!", "Hello", "Hey! How can I help?"],
    "how are you?": ["I am doing great! Thanks!", "All systems operational!"],
    "bye": ["Goodbye!", "See you soon!", "Bye!"],
}

def get_response(user_input):
    user_input = user_input.lower()
    tokens = nltk.word_tokenize(user_input)

    for key in responses.keys():
        if keys in tokens:
            return random.choice(responses[key])

    return "I'm not sure how to respond to that."

print("Chatbot: Hello! Type 'bye' to quit.")
while True:
    user_input = input("You: ")
    if user_input.lower() == "bye":
        print("Chatbot:", random.choice(responses["bye"]))
        break
    print("Chatbot:", get_response(user_input))
