#create a func to remove zeros from a list



class Solution:
    @staticmethod
    def remove_zeros(li:list) -> list:
        clean_li = []
        for el in li:
            if el != 0:
                clean_li.append(el)
        return clean_li
    
    def remove_zeros2(li:list) -> list:
        li = sorted(li,reverse=True)
        
        for el in range(len(li)-1,0,-1):
            if li[el] != 0:
                break
            li.pop()
        return li
    
lista = [0,1,2,4,0,1,2,3,45,3,0]

a = Solution.remove_zeros2(lista)
print(a)