# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return None
        if head.next == None:
            return head
        
        lenList = 0
        curr = head 
        while(curr != None):
            curr = curr.next 
            lenList += 1

        if k % lenList == 0:
            return head 

        fromStart = lenList - k % lenList 
        count = 1
        curr = head
        while(count < fromStart):
            curr = curr.next 
            count += 1
         
        rightStart = curr.next
        curr.next = None
        rightEnd = rightStart
        while(rightEnd.next != None):
            rightEnd = rightEnd.next 

        rightEnd.next = head 
        return rightStart  
