

def maxArea(height) ->int:
    maximA = -1
    left,right = 0, len(height) - 1

    while left < right:
        currArea = (right - left) * min(height[left],height[right])
        maximA = max(maximA, currArea)

        if height[left] < height[right]:
            left += 1
        else:
            right -= 1    
    return maximA

a = maxArea([1,8,6,2,5,4,8,3,7])
print(a)
