# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        curr = head
        linkedListLen = 0
        while(curr != None):
            linkedListLen += 1
            curr = curr.next
        
        diff = linkedListLen // 2 
        f, s = head, head
        while(diff > 0):
            f = f.next 
            diff -= 1
        
        while(f.next != None):
            f = f.next 
            s = s.next
        
        return s if linkedListLen % 2 != 0 else s.next 

