
from typing import List

class Solution:
    def jump(self, nums) -> int:
        l = r = 0
        jumps = 0
        goal = len(nums)-1
        while r < len(nums):  
            farthest = max(i + nums[i] for i in nums[l:r+1])    
            if goal in range(l,r+1):
                break
            jumps +=1
            temp = r
            r = farthest
            l = temp + 1
        return jumps
    
sol1 = Solution()
a = sol1.jump([2,3,1,1,4])
print(a)