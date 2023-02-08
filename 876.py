# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


from typing import Optional


class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # curr = head
        # counter = 0
        # mid_index = 0

        # while curr:
        #     counter += 1
        #     curr = curr.next

        # if counter == 1:
        #     return head

        # mid_index = counter // 2
        # curr = head
        # counter = 0

        # while curr:
        #     counter += 1
        #     curr = curr.next

        #     if counter == mid_index:
        #         return curr

        # slow = fast = head
        # while fast and fast.next:
        #     slow = slow.next
        #     fast = fast.next.next
        # return slow

        middleNode = head
        currentLength = 0
        while head:
            head = head.next
            currentLength += 1
            if currentLength % 2 == 0:
                middleNode = middleNode.next
        return middleNode
