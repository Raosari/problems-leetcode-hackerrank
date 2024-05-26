# Given a string s consisting of words and spaces,
# return the length of the larger word in the string.

import functools

class Solution:
    def large_word(self,string):
        list_of_words = string.split()
        list_of_words.sort(key=len)
        return len(list_of_words[-1])
    
    def large_word2(self,string):
        list_of_words = string.split()
        answer = functools.reduce(lambda acc,item: acc if len(acc) >= len(item) else item, list_of_words)
        return len(answer),answer
    
s = "hola pequenos como estan el dia de hoy"
problem1 = Solution()
a = problem1.large_word2(s)

print(a)