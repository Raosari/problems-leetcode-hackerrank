from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        start,end = 0, len(nums) - 1
        res = nums[0]

        while start <= end:
            if nums[start] < nums[end]:
                res = min(res, nums[start])
                break
            
            mid = start + (end-start)//2
            res = min(res, nums[mid])
            
            if nums[mid] >= nums[start]:
                start = mid + 1

            else:
                end =  mid - 1
        return res
    
nums = [4,5,6,7,0,1,2]
solve1 = Solution()
print(solve1.findMin(nums))