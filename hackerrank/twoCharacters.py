def alternate(s):
    # Write your code here
    countMap = {}
    for char in s:
        countMap[char] = countMap.get(char, 0) + 1
    list_of_val = []
    for v in countMap.values():
        list_of_val.append(v)
    list_of_val.sort()
    return sum(list_of_val[-1: -3:-1])

print(alternate("beabeefeab"))