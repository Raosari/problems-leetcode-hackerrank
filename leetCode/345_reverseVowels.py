class Solution:
    def reverseVowels(self, s: str) -> str:
        list1 = list(s)
        vowels = "aeiouAEIOU"
        pos = []
        for i, ch in enumerate(s):
            if ch in vowels:
                pos.append([ch,i])
        
        idxs = [i[1] for i in pos]
        vows = [v[0] for v in pos]

        r_vows = vows[::-1]
        new_order = [ [r_vows[i], idxs[i]] for i in range(len(idxs)) ]
        for item in new_order:
            list1[item[1]] = item[0]
        return "".join(list1)
    
sol1 = Solution()
a = sol1.reverseVowels("Hola mundo")
print(a)