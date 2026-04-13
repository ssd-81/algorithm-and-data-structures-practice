# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr1 = head
        if not curr1 or not curr1.next:
            return head 
        # curr2 = head.next
        prev = None

        while(curr1.next):
            temp = curr1.next 
            curr1.next = prev
            prev = curr1
            curr1 = temp 
        curr1.next = prev
        return curr1
            