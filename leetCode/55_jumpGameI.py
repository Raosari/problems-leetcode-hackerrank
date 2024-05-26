       
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if nums[0] == 0 and len(nums) > 1:
            return False
        
        goal = len(nums) - 1
        for i in range(len(nums)-1,-1,-1):
            if i + nums[i] >= goal:
                goal = i
        return goal == 0