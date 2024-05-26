# Given a roman numeral, convert it to an integer.

# Example 1:

# Input: s = "III"
# Output: 3
# Explanation: III = 3.

# Example 2:
# Input: s = "LVIII"
# Output: 58
# Explanation: L = 50, V= 5, III = 3.

# Example 3:
# Input: s = "MCMXCIV"
# Output: 1994
# Explanation: M = 1000, CM = 900, XC = 90 and IV = 4


def roman_to_int(string):
    letters = string.upper()
    iters = len(letters)-1
    result,previous = 0,0
    number = None
    for i in range(iters,-1,-1):
        match letters[i]:
            case "I": number = 1
            case "V": number = 5
            case "X": number = 10
            case "L": number = 50
            case "C": number = 100
            case "D": number = 500
            case "M": number = 1000
        if number >= previous:
            result += number
        else:
            result -= number
        previous = number
    return result

def roman_to_int2(string):
    letters = string[::-1]
    result = 0
    previous = 0
    roman_numbers = {
        "I":1, 
        "V":5,
        "X":10, 
        "L": 50,
        "C": 100, 
        "D": 500,
        "M": 1000 
        }
    
    for char in letters:
        number = roman_numbers[char]
        if number >= previous:
            result += number
        else:
            result -= number
        previous = number
    return result
A = roman_to_int2("XL")
print(A)
