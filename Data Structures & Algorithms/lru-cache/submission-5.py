class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.hashmap = {}
        self.head = DoublyLinkedListNode(-1, -1)
        self.tail = DoublyLinkedListNode(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head

    def remove_node(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
    
    def add_node_to_tail(self, node):
        prev = self.tail.prev
        self.tail.prev = node 
        node.prev = prev
        node.next = self.tail
        prev.next = node

    def get(self, key: int) -> int:
        if key in self.hashmap:
            node = self.hashmap[key]
            self.remove_node(node)
            self.add_node_to_tail(node)
            return node.value
        return -1

    def put(self, key: int, value: int) -> None:
        # node = DoublyLinkedListNode(key, value)
        # self.hashmap[key] = node
        # if len(self.hashmap) > self.capacity:
        #     first = self.head.next
        #     self.remove_node(first)
        #     del self.hashmap[first.key]
        # self.add_node_to_tail(node)
        if key in self.hashmap:
            self.remove_node(self.hashmap[key])
        node = DoublyLinkedListNode(key, value)
        self.hashmap[key] = node
        if len(self.hashmap) > self.capacity:
            del self.hashmap[self.head.next.key]
            self.remove_node(self.head.next)
        self.add_node_to_tail(node)
                   
class DoublyLinkedListNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = self.next = None