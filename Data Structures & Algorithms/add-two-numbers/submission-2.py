# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        prev = dummy
        cur = dummy
        carry = 0
        while l1 and l2:
            c = l1.val + l2.val + carry 
            carry = c // 10 
            cur.next = ListNode(c % 10)
            cur = cur.next

            l1 = l1.next 
            l2 = l2.next 

        while l1:
            c = l1.val + carry 
            carry = c // 10 
            cur.next = ListNode(c % 10)
            cur = cur.next

            l1 = l1.next 
            
        while l2:
            c = l2.val + carry 
            carry = c // 10 
            cur.next = ListNode(c % 10)
            cur = cur.next
            l2 = l2.next
        
        if carry > 0:
            cur.next = ListNode(carry)
            
        
        return dummy.next