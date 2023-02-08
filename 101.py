# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root.left or not root.right:
            return not root.left and not root.right

        stack_l = [root.left]
        stack_r = [root.right]

        while stack_l and stack_r:
            node_l = stack_l.pop()
            node_r = stack_r.pop()

            if node_l.val != node_r.val:
                return False

            if not node_l.left or not node_r.right:
                if node_l.left or node_r.right:
                    return False
            else:
                stack_l.append(node_l.left)
                stack_r.append(node_r.right)

            if not node_l.right or not node_r.left:
                if node_l.right or node_r.left:
                    return False
            else:
                stack_l.append(node_l.right)
                stack_r.append(node_r.left)

        return not stack_l and not stack_r

        # def isSym(L, R):
        #     if not L or not R:
        #         return not L and not R

        #     if L and R and L.val == R.val:
        #         return isSym(L.left, R.right) and isSym(L.right, R.left)

        #     return False

        # return isSym(root, root)
