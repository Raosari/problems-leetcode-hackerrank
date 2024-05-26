

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle) == 0:
            return 0
        haystack.find(needle)
        for i in range(len(haystack) - len(needle) + 1):
            for j in range(len(needle)):
                if haystack[i+j] != needle[j]:
                    break
                if j == len(needle) -1:
                    return i
        return -1    



sol1 = Solution()
a = sol1.strStr('heeloso','lo')
print(a)