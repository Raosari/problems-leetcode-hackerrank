from typing import List
from functools import reduce

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        smaller = reduce(lambda a,b: a if len(a) <= len(b) else b,strs)
        qty = 0
        for i in range(len(smaller)):
            for s in strs:
                if s[i] != smaller[i]:
                    return smaller[0:i]
            qty += 1
        return smaller[0:qty]

    

sol1 = Solution()
a = sol1.longestCommonPrefix(['eaaaaa','ea','eaaa','eiaeacccccc','ea','ea'])
print(a)