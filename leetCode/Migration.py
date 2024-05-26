
def migratoryBirds(arr):
    # Write your code here
    if len(arr) == 0:
        return None
    countOfBirds = {}
    maxF = 0
    for i in arr:
        try:
            countOfBirds[i] = countOfBirds.get(i, 0) + 1
            currM = countOfBirds[i]
            maxF = max(maxF, currM)
        except:
            return 'All elements must be an integer'
    max_types = [k for k, v in countOfBirds.items() if v == maxF]
    return min(max_types)
    
print(migratoryBirds([1,0,"a"]))