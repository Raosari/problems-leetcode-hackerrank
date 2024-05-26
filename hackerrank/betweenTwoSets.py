def getTotalX(a, b):
    # Write your code here
    numbers = sorted(a + b)
    count = 0
    for num in range(numbers[0], numbers[-1]+1):
        for i in range(len(numbers)):
            if numbers[i] % num != 0:
                break
            if i == len(numbers):
                count += 1
    return count  



print(getTotalX([2,4],[16,32,96]))