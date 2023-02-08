# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from typing import Optional
from collections import deque


class Solution:
    def mergeTrees(
        self, root1: Optional[TreeNode], root2: Optional[TreeNode]
    ) -> Optional[TreeNode]:
        if root1 and root2:
            node: TreeNode() = TreeNode(root1.val + root2.val)
            node.left = self.mergeTrees(root1.left, root2.left)
            node.right = self.mergeTrees(root1.right, root2.right)
            return node
        else:
            return root1 or root2

        # if not root1:
        #     return root2

        # queue = deque()
        # queue.append([root1, root2])

        # while queue:
        #     curr = queue.popleft()

        #     if not curr[1]:
        #         continue

        #     curr[0].val += curr[1].val

        #     if not curr[0].left:
        #         curr[0].left = curr[1].left
        #     else:
        #         queue.append([curr[0].left, curr[1].left])

        #     if not curr[0].right:
        #         curr[0].right = curr[1].right
        #     else:
        #         queue.append([curr[0].right, curr[1].right])

        # return root1
