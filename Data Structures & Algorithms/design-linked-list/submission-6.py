class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next 


class MyLinkedList:

    def __init__(self):
        self.dummy = ListNode()        

    def get(self, index: int) -> int:
        node = self.dummy 
        i = -1
        while node and i != index - 1:
            node = node.next 
            i += 1
        if node and node.next:
            return node.next.val
        return -1


    def addAtHead(self, val: int) -> None:
        nxt = self.dummy.next 
        newNode = ListNode(val)
        self.dummy.next = newNode
        newNode.next = nxt 


    def addAtTail(self, val: int) -> None:
        node = self.dummy
        while node.next:
            node = node.next 
        node.next = ListNode(val)


    def addAtIndex(self, index: int, val: int) -> None:
        i = -1 
        node = self.dummy

        while node and i != (index -1):
            node = node.next 
            i += 1
        if node:
            nxt = node.next 
            newNode = ListNode(val)
            newNode.next = nxt 
            node.next = newNode

    def deleteAtIndex(self, index: int) -> None:
        i = -1
        node = self.dummy 

        while node and i != (index -1):
            node = node.next
            i += 1
        if node and node.next:
            node.next = node.next.next if node.next else None


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)