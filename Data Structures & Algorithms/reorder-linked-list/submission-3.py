# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # [ 0 , n - 1, 1, n -2 , 2, n -3]
        # reordering has to be done 
        # I have some confusion regarding linked list 
        # but I will try anyway 

        # can I brute force this , likely not 
        # a bit of optimization is required 

        # how will I get to the last node 
        # next - next till curr.next != None 
        
        arr = []
        curr = head
        while curr != None:
            arr.append(curr)
            curr = curr.next
        # we have gotten all the nodes in the list now 
        # can we use two pointers now 
        l, r = 0, len(arr) -1 
        newArr = []
        while l <= r:
            if l != r:
                newArr.append(arr[l])
                newArr.append(arr[r])
            else:
                newArr.append(arr[l])
            l += 1
            r -= 1
        
        for n in range(len(arr) - 1) :
            newArr[n].next = newArr[n + 1]
        newArr[len(newArr) - 1].next = None

        


















