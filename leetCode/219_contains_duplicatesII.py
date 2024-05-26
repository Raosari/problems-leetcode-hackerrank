from typing import List

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        hashmap = {}
        for i in range(len(nums)):
            if nums[i] not in hashmap:
                hashmap[nums[i]] = i
            elif abs(hashmap[nums[i]] - i) <= k:
                    return True
            else:
                hashmap[nums[i]] = i 
        return False
sol1 = Solution()
a = sol1.containsNearbyDuplicate([0,0,1,1],1)
print(a)