class Solution:
    def _badReplace(text, old, new):
        new_string = ''
        i = 0
        while i < (len(text) - len(old) + 1):
            if text[i:i+len(old)] == old:
                new_string += new
                i += len(old)
            else:
                new_string += text[i]
                i += 1
        return new_string
    
    def convert(self,num_of_a:int) -> str:
        string = 'a'*num_of_a
        alph = 'abcdefghijklmnopqrstuvwxyz'

        # This is going to create a dic like: 'aa':'b', 'bb':c...'yy':'z' 
        charsMap = { 2*char: alph[idx+1] for idx,char in enumerate(alph[:-1]) }
        
        for chars in charsMap.keys():
            # string = string.replace(chars,charsMap[chars])
            string = Solution._customRep(string,chars, charsMap[chars])
        return string
        
        # for chars in charsMap.keys():
        #     string2 = charsMap[chars].join(string2.split(chars))
        # return string2
    

sol1 = Solution()
a = sol1.convert(10000) 
print(a)