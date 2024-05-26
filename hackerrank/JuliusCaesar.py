

def caesarCipher(s,k):
    alph = 'abcdefghijklmnopqrstuvwxyz'
    rotated_alph = alph[k % 26:] + alph[:k % 26]
    res = ''
    for char in s:
        if not char.isalpha():
            res += char
        elif char.islower():
            res += rotated_alph[alph.find(char)]
        elif char.isupper():
            res += rotated_alph[alph.find(char.lower())].upper()
    return res


print(caesarCipher("www.abc.xy",2))
print(87%26)