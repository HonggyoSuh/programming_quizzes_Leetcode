# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        return max((self.maxDepth(root.left)), (self.maxDepth(root.right))) + 1

        # if not root: return 0

        # queue = deque([root])
        # num_node_level = 1
        # levels = 0

        # while queue:
        #     node = queue.popleft()
        #     if node.left:
        #         queue.append(node.left)
        #     if node.right:
        #         queue.append(node.right)
        #     num_node_level -= 1
        #     if num_node_level == 0:
        #         levels += 1
        #         num_node_level = len(queue)

        # return levels
