# Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. 
# The order of the elements may be changed. Then return the number of elements in nums which 
# are not equal to val.
from typing import List
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        r = len(nums) - 1
        l = 0
        while l <= r:
            while nums[l] == val and r >= 0:
                temp = nums[l]
                nums[l] = nums[r]
                nums[r] = temp
                r -= 1
            l += 1
        return l
sol1 = Solution()
a = sol1.removeElement([1,2],1)
print(a)

