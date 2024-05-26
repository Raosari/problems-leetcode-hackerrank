from typing import List

class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        count = nums[0]
        for i in range(1,len(nums)):
            if nums[i]==nums[i-1]+1:
                count+= nums[i]
            else:
                break
        while True:
            if count not in nums:
                return count
            else:
                count+=1
    
solution1 = Solution()
a = solution1.missingInteger()
print(a)
