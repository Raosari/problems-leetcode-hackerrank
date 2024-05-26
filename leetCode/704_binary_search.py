# Given an array of integers nums which is sorted in ascending order, and an integer target, 
# write a function to search target in nums.
# If target exists, then return its index. Otherwise, return -1.

# You must write an algorithm with O(log n) runtime complexity.

from typing import List

class Solution:
    def search(self, nums:List[int], target:int) -> int:
        start,end = 0, len(nums) - 1
        while start <= end:
            mid = start + (end-start)//2
            if target == nums[mid]:
                return mid
            elif target < nums[mid]:#left side
                end = mid - 1
            else:
                start = mid + 1
        return -1

solution1 = Solution()
print(solution1.search([-1,0,3,5,9,12],1))