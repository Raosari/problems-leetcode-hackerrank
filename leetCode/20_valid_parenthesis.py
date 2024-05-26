# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']',
#  determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.
from collections import deque

class Solution:
    def isValid(self, s: str) -> bool:
        ClosebracketsMap = {
            ')' : '(',
            ']' : '[',
            '}' : '{',
        }
        OpenBrackets = set({'(','[','{'})
        stack = deque()
        
        for bracket in s:
            if bracket in OpenBrackets:
                stack.append(bracket)
            elif len(stack) == 0 or ClosebracketsMap[stack.pop()] != bracket:
                return False
        
        return True if len(stack) == 0 and len(s)>1 else False
              
sol1 = Solution()
a = sol1.isValid("[{}]")
print(a)