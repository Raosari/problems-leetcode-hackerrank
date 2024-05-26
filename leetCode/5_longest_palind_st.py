class Solution:
    def longestPalindrome(self, s: str) -> str:
        resLen = 0

        for i in range(len(s)):
            #odd
            l,r = i,i
            while l >= 0 and r<len(s) and s[l] == s[r]:
                if (r - l + 1) > resLen:
                    resl,resr = l,r
                    resLen = r-l+1

                l-=1
                r+=1
            l,r = i,i+1
            #even
            while l >=0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > resLen:
                    resl,resr = l,r
                    resLen = r - l + 1
                l -= 1
                r += 1            
        return s[resl:resr+1]

sol1 = Solution()
a = sol1.longestPalindrome("cbbd")
print(a)    