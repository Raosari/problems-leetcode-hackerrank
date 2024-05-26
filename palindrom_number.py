# build a function that return if a number is a palindrom
#try to not convert the number into a string

def is_palindrom(num):
    original = num
    inver = 0
    
    while num > 0:
        digit = num % 10
        inver = inver * 10 + digit
        num = num // 10
    
    return original == inver

a = is_palindrom(121)
print(a)