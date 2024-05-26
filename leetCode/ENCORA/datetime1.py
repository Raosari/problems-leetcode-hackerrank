def countApplesAndOranges(s, t, a, b, apples, oranges):
    # Write your code here
    count_apples = 0
    count_oranges = 0
    shoots = apples + oranges
    for i, d in enumerate(shoots, start=1):
        point = a + d
        if point >= s and point <= t:
            if i <= len(apples):
                count_apples += 1
            else:
                count_oranges += 1

    print(count_apples)
    print(count_oranges)

print(countApplesAndOranges(2,3,1,5,[2],[-2]))