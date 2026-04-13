# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        auxilliary = ListNode()
        auxilliary.next = head

        if not head or not head.next:
            return None

        trailer, leader = auxilliary, auxilliary 
        for _ in range(n):
            leader = leader.next 
        
        while leader and leader.next:
            trailer = trailer.next 
            leader = leader.next 
        trailer.next = trailer.next.next if trailer.next else None
        return auxilliary.next
        