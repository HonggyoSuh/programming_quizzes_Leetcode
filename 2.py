from tkinter.tix import ListNoteBook
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNoteBook], l2: Optional[ListNode]) -> Optional[ListNode]:
        first = ""
        while (l1 != None):
            first += str(l1.val)
            l1 = l1.next
        
        second = ""
        while (l2 != None):
            second += str(l2.val)
            l2 = l2.next
        
        first = first[::-1]
        second = second[::-1]

        first = int(first)
        second = int(second)
        result = first + second
        result = str(result)
        result = result[::-1]
        result = list(result)

        initial = ListNode()
        initial.val = result[0]
        curr = initial

        for i in range(1, len(result)):
            newLink = ListNode(result[i])
            curr.next = newLink
            curr = curr.next

        return initial

        