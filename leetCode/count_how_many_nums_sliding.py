


class Solution:
    def CountNumbers(self,li:list):
        numbers = {}
        left = 0  # Left pointer of the window
        
        for right in range(len(li)):
            while li[left] != li[right]:
                left += 1  # Shrink the window from the left if it doesn't contain the current number
            numbers[li[right]] = right - left + 1  # Update the count for the current number
        return numbers


sol1 = Solution()
a = sol1.CountNumbers([1,1,2,2,3,4,5,5,5,5])
print(a)