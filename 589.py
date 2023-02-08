# Definition for a Node.
from typing import List


class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        nums = list()

        if root == None:
            return

        nums.append(root.val)
        for i in root.children:
            nums += Solution().preorder(i)
            
        return nums
