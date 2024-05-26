class Solution:
    def reverse(self, x: int) -> int:
        if 2**31 -1 < x < -2**31:
            return 0
        
        reversed_num = int(str(abs(x))[::-1])

        if reversed_num > 2**31-1:
            return 0

        elif x >= 0:
            return reversed_num
        else: 
            return  reversed_num * -1
        
    
sol1 = Solution()
print(sol1.reverse(-21))
