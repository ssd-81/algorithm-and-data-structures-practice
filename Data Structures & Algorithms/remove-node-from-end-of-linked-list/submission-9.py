# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr = ListNode()
        curr.next = head
        f = curr
        # if not head:
        #     return head
        # if not head.next:
        #     return head.next
        curr2 = curr

        i = 0
        while(i < n):
            curr2 = curr2.next
            i += 1
        
        while curr2.next:
            curr = curr.next
            curr2 = curr2.next 
        curr.next = curr.next.next 
        return f.next
        