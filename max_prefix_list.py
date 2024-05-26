# given an array return the max prefix possible in all items
# example [apple, app, api] return ap
# [and, annie, ocon] return false


def max_prefix(arr):
    arr.sort()
    first = arr[0]
    last = arr[-1]
    out = ""
    m_range = len(first) == min(len(first),len(last))
    counter = 0

    for char in first if m_range else last:
        if first[counter] == last [counter]:
            out += char
            counter += 1
    if counter > 0:   
        return out
    else:
        return False
    
array = ["apple","","apple"]
a = max_prefix(array)

print(a)