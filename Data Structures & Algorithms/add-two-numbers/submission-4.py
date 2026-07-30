# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        carry = 0
        dummy = ListNode()
        curr = dummy 

        while l1 or l2 or carry:
            currVal = 0 
            if l1:
                currVal += l1.val 
                l1 = l1.next 
            if l2:
                currVal += l2.val
                l2 = l2.next 

            currVal += carry 
            carry = currVal // 10
            curr.next = ListNode(currVal % 10)
            
            curr = curr.next 
        return dummy.next