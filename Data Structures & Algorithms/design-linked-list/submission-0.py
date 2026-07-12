class LinkedListNode:
    def __init__(self, val=0, next=None):
        self.val = val 
        self.next = next


class MyLinkedList:
    def __init__(self):
        self.dummy_head = LinkedListNode(-1, None)

    def get(self, index: int) -> int:
        curr = self.dummy_head
        i = -1
        while i != index and curr:
            curr = curr.next 
            i += 1
        return curr.val 


    def addAtHead(self, val: int) -> None:
        nxt = self.dummy_head.next 
        self.dummy_head.next = LinkedListNode(val, nxt)
        

    def addAtTail(self, val: int) -> None:
        
        curr = self.dummy_head
        while curr.next:
            curr = curr.next 
        curr.next = LinkedListNode(val)

    def addAtIndex(self, index: int, val: int) -> None:
        # stop at index - 1
        i = -1
        curr = self.dummy_head
        while i != (index -1) and curr:
            curr = curr.next
            i += 1 
        nxt = curr.next 
        curr.next = LinkedListNode(val, nxt)  

    def deleteAtIndex(self, index: int) -> None:
        i = -1
        curr = self.dummy_head
        while i != (index -1) and curr:
            curr = curr.next 
            i += 1
        curr.next = curr.next.next # could throw error : x -> y (not sure)


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)