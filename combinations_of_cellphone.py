class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        digits_d = {
            '2':'abc', 
            '3':'def',
            '4':'ghi', 
            '5':'jkl', 
            '6':'mno', 
            '7':'pqrs',
            '8':'tuv',
            '9':'wxyz'
        }


        def backTrack():
            pass