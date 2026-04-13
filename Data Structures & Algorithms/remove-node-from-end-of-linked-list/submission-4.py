# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummyNode = ListNode(None, head)

        l = dummyNode
        r = head

        i = 0
        while (i < n - 1 and r):
            r = r.next
            i += 1
        

        while(r.next):
            r = r.next
            l = l.next

        l.next = l.next.next
        return dummyNode.next 