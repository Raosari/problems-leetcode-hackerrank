class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res = ""
        major = max(len(word1), len(word2))
        for i in range(major):
            if i < len(word1):
                res += word1[i]
            if i < len(word2):
                res += word2[i]
        return res

sol1 = Solution()
a = sol1.mergeAlternately("abc","defe")
print(a)