# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        curr_node, prev_node = head, None

        while curr_node:
            if curr_node.val == val:
                if curr_node == head:
                    curr_node = head = head.next
                else:
                    prev_node.next = curr_node.next
                    curr_node = curr_node.next
            else:
                prev_node = curr_node
                curr_node = curr_node.next

        return head
