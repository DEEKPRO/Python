import roman as r

rom = input("Enter a Roman numeral to convert to a normal number: ")

num = r.fromRoman(rom)
print(num)

"""
rom = input("Enter a Roman numeral to convert to a normal number: ")

def roman_to_int(rom):
    roman_numerals = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    result = 0
    for i in range(len(rom)-1):
        if roman_numerals[rom[i]] < roman_numerals[rom[i + 1]]:
            result -= roman_numerals[rom[i]]
        else:
            result += roman_numerals[rom[i]]
    return result + roman_numerals[rom[-1]]

print(roman_to_int(rom))"""