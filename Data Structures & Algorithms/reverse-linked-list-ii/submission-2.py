# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        
        # three phase solution 
        aux_head = ListNode(-1, head)
        currNode = head
        prev = aux_head 
         
        
        for _ in range(left-1):
            prev, currNode = currNode, currNode.next 
        
        lP = prev 
        prev = None
        for _ in range(right - left + 1):
            tmpNext = currNode.next 
            currNode.next = prev 
            prev = currNode 
            currNode = tmpNext 

        lP.next.next = currNode 
        lP.next = prev
        
        return aux_head.next 