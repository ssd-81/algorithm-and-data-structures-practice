# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head == None or head.next == None:
            return False 
        slow, fast = head, head.next 

        while(True):
            if slow == fast:
                return True
            if fast and fast.next:
                slow = slow.next 
                fast = fast.next.next
            else:
                return False 

        return False 

        