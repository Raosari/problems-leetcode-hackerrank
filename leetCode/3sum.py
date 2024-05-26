# Given an integer array nums, return all the triplets
# [nums[i], nums[j], nums[k]] such that 
# i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

# Notice that the solution set must not contain duplicate triplets.

from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]: 
        res = []
        nums.sort()

        for i,num in enumerate(nums):
            if i > 0 and num == nums[i - 1]:
                continue
                
            l,r = i+1,len(nums)-1
            while l<r:
                cur_sum = num + nums[l] + nums[r]
                if cur_sum > 0:
                    r -= 1
                elif cur_sum < 0:
                    l += 1
                else:
                    res.append([num,nums[l],nums[r]])
                    l += 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
        return res
    
sol1 = Solution()
a = sol1.threeSum([0,0,0])
print(a)