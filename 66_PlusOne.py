
# You are given a large integer represented as an 
# integer array digits, where each digits[i] is the 
# ith digit of the integer. The digits are ordered
# from most significant to least significant in left-to-right order.
# The large integer does not contain any leading 0's.
from typing import List
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        res = ''
        for el in digits:
            res += str(el)
        ans = str(int(res) + 1)

        k = []
        for i in range(len(ans)):
            k.append(int(ans[i]))
        return k
    

sol1 = Solution()
a = sol1.plusOne([1,4,3,9])
print(a)