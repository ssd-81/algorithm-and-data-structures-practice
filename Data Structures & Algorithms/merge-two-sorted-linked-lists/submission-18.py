# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        newHead = ListNode(0, None)
        curr = newHead

        first = list1
        second = list2

        while(first and second):
            if first.val > second.val:
                curr.next = second
                curr = curr.next
                second = second.next
            else:
                curr.next = first
                curr = curr.next 
                first = first.next  
        while(first):
            curr.next = first
            curr = curr.next
            first = first.next
        while(second):
            curr.next = second
            curr = curr.next 
            second = second.next 
        return newHead.next 