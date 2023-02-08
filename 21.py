# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# class Solution:
#     def mergeTwoLists(
#         self, list1: Optional[ListNode], list2: Optional[ListNode]
#     ) -> Optional[ListNode]:
#         if list1 == None:
#             return list2
#         elif list2 == None:
#             return list1

#         merged_list = list()

#         curr = list1
#         self.appendList(merged_list, curr)
#         curr = list2
#         self.appendList(merged_list, curr)
#         merged_list.sort()

#         merged_linked_list = ListNode(val=0, next=None)
#         curr = merged_linked_list
#         for index, i in enumerate(merged_list):
#             curr.val = i
#             if index < len(merged_list) - 1:
#                 curr.next = ListNode(val=0, next=None)
#             curr = curr.next

#         return merged_linked_list

#     def appendList(self, merged_list: list[int], curr: Optional[ListNode]):
#         while curr != None:
#             merged_list.append(curr.val)
#             curr = curr.next

# ////////////////////////////////////////////////////////
# result = curr = ListNode(0)

# while list1 and list2:
#     if list1.val < list2.val:
#         curr.next = list1
#         list1 = list1.next
#     else:
#         curr.next = list2
#         list2 = list2.next
#     curr = curr.next

# curr.next = list1 or list2
# return result.next
