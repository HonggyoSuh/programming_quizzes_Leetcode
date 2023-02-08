# Definition for a binary tree node.
from collections import deque
from typing import Deque, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        queue: Deque[TreeNode] = deque([root])
        result: int = 0

        while queue:
            node = queue.popleft()
            if node.left:
                if node.left.left or node.left.right:
                    queue.append(node.left)
                else:
                    result += node.left.val
            if node.right:
                if node.right.left or node.right.right:
                    queue.append(node.right)

        return result
