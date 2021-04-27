# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 == None or l2 == None:
            return l2 if l1 == None else l1
        first = parent = l1 if l1.val <= l2.val else l2
        second = l2 if first == l1 else l1
        while first.next != None and second != None:
            if first.val <= second.val <= first.next.val:
                store = second.next
                second.next = first.next
                first.next = second
                second = store
            first = first.next
        if not second == None:
            first.next = second
        return parent
