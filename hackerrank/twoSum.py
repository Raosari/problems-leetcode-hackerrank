

def twoSum(arr, target):
    numsMap = {}
    for idx, n in enumerate(arr):
        num_to_find = target - n
        if num_to_find in numsMap:
            return [numsMap[num_to_find],idx]
        else:
            numsMap[n] = idx
    return -1

print(twoSum([1,3,7,9,2],22))


