# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        # hash map storing the nodes
        hashSet = {}
        temp = head
        while temp.next != None:
            if temp in hashSet:
                return True
            else:
                hashSet[temp] = True
            temp = temp.next 
        return False

