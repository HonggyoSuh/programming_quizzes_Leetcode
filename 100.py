# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from typing import Optional


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # if p and q:
        #     return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        # return p is q

        # def t(n):
        #     return n and (n.val, t(n.left), t(n.right))

        # return t(p) == t(q)

        # return p and q and p.val == q.val and all(map(self.isSameTree, (p.left, p.right), (q.left, q.right))) or p is q

        if not p or not q:
            return not p and not q

        stack_p = [p]
        stack_q = [q]

        while stack_p and stack_q:
            element_p = stack_p.pop()
            element_q = stack_q.pop()

            if element_p.val != element_q.val:
                return False

            if not element_p.right or not element_q.right:
                if element_p.right or element_q.right:
                    return False
            else:
                stack_p.append(element_p.right)
                stack_q.append(element_q.right)

            if not element_p.left or not element_q.left:
                if element_p.left or element_q.left:
                    return False
            else:
                stack_p.append(element_p.left)
                stack_q.append(element_q.left)

        return not stack_p and not stack_q
