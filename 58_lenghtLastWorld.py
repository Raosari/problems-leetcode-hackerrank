class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.upper()
        k = 0
        print("" in "ABC")
        prev = " "
        alphabet = set({
            'A', 'B', 'C', 'D', 'E',
            'F', 'G', 'H', 'I', 'J', 
            'K', 'L', 'M', 'N', 'O', 
            'P', 'Q', 'R', 'S', 'T', 
            'U', 'V', 'W', 'X', 'Y',
            'Z'
        })
    
        for i in range(len(s)-1,-1,-1):
            if prev in alphabet and s[i] == " ":
                break
            if s[i] != " ":
                k+=1
            prev = s[i]
        return k

sol1 = Solution()
a = sol1.lengthOfLastWord("   fly me   to   the moon  ")
print(a)