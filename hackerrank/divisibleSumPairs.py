

def divisiblePairs(arr,k):
    pairs = 0
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if (arr[i] + arr[j]) % k == 0:
                pairs += 1
    return pairs
