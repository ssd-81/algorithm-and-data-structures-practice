# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:

        curr = 1
        currNode = head
        prev = None

        while curr != left:
            curr += 1
            prev = currNode 
            currNode = currNode.next 

        l_head = currNode 
        
        while curr != right:
            curr += 1
            nxt = currNode.next 
            currNode.next = prev
            prev = currNode 
            currNode = nxt

        r_head = currNode 
        nxt = currNode.next
        currNode.next = prev 

        l_head.next = nxt 
        return r_head 

         

         
