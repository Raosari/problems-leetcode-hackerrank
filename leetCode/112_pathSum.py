# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
from typing import Optional


class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        stack = deque()
        visited = set()
        stack.append(root)
        CurSum = 0
        while stack:
            i = stack.pop()
            visited.add(i)
            
            CurSum += i.val
            
            if not node.left and not node.right:




        