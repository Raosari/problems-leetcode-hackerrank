# Given an array of integers nums and an integer target, 
# return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, 
# and you may not use the same element twice.
# You can return the answer in any order.

class Solution():
    def TwoSum(self,numbers, target):
        hmap = {}

        for idx, number in enumerate(numbers): 
            lookup = target - number
            if lookup in hmap:
                return hmap[lookup],idx
            else:
                hmap[number] = idx
        return
    
    def TwoSum2(self,numbers,target):
            hmap = {num:idx for idx,num in enumerate(numbers)}
            for i in range(len(numbers)):
                lookfor = target - numbers[i]
                if lookfor in hmap and lookfor != numbers[i]:
                        return i, hmap[lookfor]
            

solution1 = Solution()
print(solution1.TwoSum2([3,2,4],6))