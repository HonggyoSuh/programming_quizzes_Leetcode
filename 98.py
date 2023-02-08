# Definition for a binary tree node.
from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        result = []
        queue = deque()
        queue.append((root, False))

        while queue:
            curr = queue.pop()

            if not curr[0]:
                continue

            if curr[1]:
                if result and curr[0].val <= result[-1]:
                    return False
                result.append(curr[0].val)
            else:
                queue.append((curr[0].right, False))
                queue.append((curr[0], True))
                queue.append((curr[0].left, False))

        return True
