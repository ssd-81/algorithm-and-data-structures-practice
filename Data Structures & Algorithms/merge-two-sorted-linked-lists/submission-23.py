# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        newHead = ListNode(0, None)
        cur = newHead
        first = list1
        second = list2

        while(first and second):
            if(first.val < second.val):
                cur.next = first
                cur = cur.next 
                first = first.next
            else:
                cur.next = second
                cur = cur.next 
                second = second.next 
        while(first):
            cur.next = first
            first = first.next
            cur = cur.next 
        while(second):
            cur.next = second
            second = second.next 
            cur = cur.next 
        return newHead.next 