# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        # curr_A = headA
        # curr_B = headB

        # while not curr_A: 
        #     curr_A = curr_A.next if curr_A else headB
        #     curr_B = curr_B.next if curr_B else headA
        #     if curr_A == curr_B:
        #         return curr_A
        # return None
        ptr_A = headA
        ptr_B = headB

        while ptr_A != ptr_B:
            ptr_A = ptr_A.next if ptr_A else headB
            ptr_B = ptr_B.next if ptr_B else headA

        return ptr_A