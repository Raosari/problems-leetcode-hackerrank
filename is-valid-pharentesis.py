# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']'
#  determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.

def isValid(string):
    calls = []
    closed_par = {
                ")":"(",
                "}":"{",
                "]":"["
    }

    for elem in string:
        if elem in closed_par:
            if not calls or closed_par[elem] != calls.pop():
                    return False
            else:
                calls.append(elem)
    return not calls


string = "{}{}()"
a = isValid(string)
print(a)