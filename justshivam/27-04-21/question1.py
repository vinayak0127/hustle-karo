# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        back = forw = head
        for i in range(n):
            forw = forw.next
        if forw == None:
            return head.next
        while not forw.next == None:
            forw = forw.next
            back = back.next
        back.next = back.next.next
        return head
