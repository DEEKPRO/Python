inp = int(input("Enter the number: "))

"""print(generate_response(f"find the factorial of this number: {inp}", temperature=0.1, max_tokens=256))"""

def factorial(number):
    if number == 1:
        return 1
    else:
        return number * factorial(number-1)
print(factorial(inp))