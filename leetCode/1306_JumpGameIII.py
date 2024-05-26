from collections import deque

class Solution:
    def JumpGame(Self, arr,start):
        siz = len(arr)
        visited = set()
        stack = deque()
        stack.append(start)

        while stack:
            i = stack.pop()
            visited.add(i)
            print((i,arr[i]),end=" ")
            if arr[i] == 0:
                return True

            for jump in (i - arr[i], i + arr[i]):
                if 0 <= jump < siz and jump not in visited:
                    stack.append(jump)
        return False  

sol1 = Solution()
a = sol1.JumpGame([1,2,2,1,3,1,2,3,4,2,0,1,2],1)
print(a)