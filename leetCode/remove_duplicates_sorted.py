from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l = 1
        for r in range(len(nums)):
            if nums[r] != nums[r-1]:
                nums[l] = nums[r]
                l += 1
        return l

    
s1 = Solution()
a = s1.removeDuplicates([1,1,2])
print(a)