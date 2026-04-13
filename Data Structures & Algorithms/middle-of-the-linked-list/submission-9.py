# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head 
        lenLinkedList = 0 
        while(slow != None):
            lenLinkedList += 1
            slow = slow.next 
        
        midVal = lenLinkedList // 2 
        slow, fast = head, head 
        while(midVal > 0):
            fast = fast.next
            midVal -= 1

        while(fast.next != None):
            slow = slow.next 
            fast = fast.next 
        return slow if lenLinkedList % 2 != 0 else slow.next 