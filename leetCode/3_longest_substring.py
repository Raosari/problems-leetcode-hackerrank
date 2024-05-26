class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_sub = 0
        for idx, char in enumerate(s):
            chars = {char:1}
            curr_substring = 1

            for p in range(idx+1, len(s)):
                if s[p] not in chars:
                    chars[s[p]] = 1
                    curr_substring += 1
                else:
                    break
            
            max_sub = max(curr_substring,max_sub)
        return max_sub
    
    def lengthOfLongestSubstring2(self,s:str) ->int:
        charSet = set()
        maxS = 0
        l= 0
        for r in s:
            while r in charSet:
                charSet.remove(s[l])
                l += 1
            charSet.add(r)
            maxS = max(maxS,len(charSet))
        return maxS

sol1 = Solution()
a = sol1.lengthOfLongestSubstring2("pwwkew")
print(a)