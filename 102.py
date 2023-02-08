# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        result, stack = [], [root]

        while stack:
            result.append([node.val for node in stack])
            stack = [leaf for node in stack for leaf in (node.left, node.right) if leaf]
            # temp = []

            # for node in stack:
            #     temp.extend([node.left, node.right])

            # stack = [leaf for leaf in temp if leaf]

        return result
