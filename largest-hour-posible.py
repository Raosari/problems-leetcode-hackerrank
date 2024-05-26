# Given an array arr[] having 4 integer digits only. 
# The task is to return the maximum 24 hour time that can be formed
#  using the digits from the array. 

# Note that the minimum time in 24 hour format is 00:00,
#  and the maximum is 23:59. If a valid time cannot be formed then return -1.

# Examples: 
# Input: arr[] = {1, 2, 3, 4} 
# Output: 23:41
# Input: arr[] = {5, 5, 6, 6} 
# Output: -1 

from itertools import permutations

def largestHourPossible(digits):   
    max_time = -1
    # return  [el for el in listaDeHoras]
    for elements in permutations(digits):
        hours = elements[0]*10 + elements[1]
        minutes = elements[2]*10 + elements[3]

        if 0 <= hours <= 23 and 0 <= minutes <= 59:
            current_time = hours*60 + minutes
            max_time = max(current_time,max_time)

    return max_time if max_time == -1 else f"{max_time//60}:{max_time % 60}"

a = largestHourPossible([1,2,3,4])
print(a)







