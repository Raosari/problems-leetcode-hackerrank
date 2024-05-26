class Solution():
    def TwoSum(self,numbers, target):
        indexedList = [(value, index) for index, value in enumerate(numbers)]
        indexedList.sort(key=lambda x: x[0])
        print(indexedList)
        left,right = 0, len(indexedList)-1
        results = []
        
        while left < right:
            sum = indexedList[left][0] + indexedList[right][0]
            if sum == target:
                results.append(indexedList[left][1]) 
                results.append(indexedList[right][1])
                left += 1 
                right -= 1  

            elif sum < target:
                left += 1 
            else:
                right -= 1
        return results
    
list1 = [2,7,11,15]
list2 = [3,2,4]
list3 = [3,3]

NewObj = Solution()
NewObj2 = Solution()
NewObj3 = Solution()

print(NewObj.TwoSum(list1,9))
print(NewObj2.TwoSum(list2,6))
print(NewObj3.TwoSum(list3,6))

