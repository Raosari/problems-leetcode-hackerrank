
def Solution(input,k):
    if len(input) > k:
        return -1
    
    odd_cap = 0
    even_cap = 0
    result = 0
    for idx, char in enumerate(input,start=1):
        if not char.isalpha():
            return -1        
        if char.isupper():
            if idx % 2 == 0:
                even_cap += 1
            else:
                odd_cap += 1
            if odd_cap > 1 or even_cap > 1:
                return -1 
        result += ord(char)
    return result
