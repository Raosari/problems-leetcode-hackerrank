from typing import List
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        av = [0] + flowerbed + [0]
        for i in range(1, len(flowerbed) + 1):
            if av[i] == 0:
                if (av[i-1] == 0 and av[i+1] == 0):
                    n -= 1
                    av[i] = 1
            if n == 0:
                return True
        return False


sol1 = Solution()
a = sol1.canPlaceFlowers([1,0],1)
print(a)