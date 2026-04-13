# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        curr = head
        lenOfLinkedList = 0 
        while curr:
            curr = curr.next
            lenOfLinkedList += 1
        midPoint = lenOfLinkedList // 2
        curr = head
        i = 0 
        while i < midPoint :
            curr = curr.next
            i += 1
        return curr 