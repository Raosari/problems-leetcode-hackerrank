class Solution:
    def climbStairs(self, n: int) -> int:
        stack = []
        visited = set()
        stack.append(0)
        count = 0
        while stack:
            i = stack.pop()
            visited.add(i)
            for next_node in (i+1,i+2):
                if next_node not in visited and next_node <= n:
                    stack.append(next_node)
        return count
sol1 = Solution()
a = sol1.climbStairs(100)
print(a)