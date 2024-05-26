from typing import List
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        numbers_map = {}
        for num in nums:
            if num not in numbers_map:
                numbers_map[num] = 1
            else:
                numbers_map[num] += 1
                return num
            
sol1 = Solution()
a = sol1.findDuplicate([1,3,4,2,2])
print(a)