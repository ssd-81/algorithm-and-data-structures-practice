class ListNode:
    def __init__(self,key, val):
        self.key = key 
        self.val = val
        self.next = None
        self.prev = None 

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity 
        self.hashMap = {} # key to node mapping 
        self.head = ListNode(-1, -1)
        self.tail = ListNode(-1, -1)
        self.head.next = self.tail 
        self.tail.prev = self.head 
        
    def add_to_start(self, node) -> None:
        node.next = self.head.next 
        self.head.next.prev = node 
        self.head.next = node 
        node.prev = self.head

        self.hashMap[node.key] = node

    def add_to_end(self, node:ListNode) -> None:

        node.prev = self.tail.prev 
        self.tail.prev.next = node
        self.tail.prev = node 
        node.next = self.tail 

        self.hashMap[key] = node  
    
    def remove_node(self,node:ListNode)->None:
        node.prev.next = node.next 
        node.next.prev = node.prev 


    def get(self, key: int) -> int:
        if key in self.hashMap:
            self.remove_node(self.hashMap[key])
            self.add_to_start(self.hashMap[key])
        return -1 if key not in self.hashMap else self.hashMap[key].val

    def put(self, key: int, value: int) -> None:
        if key in self.hashMap:
            self.remove_node(self.hashMap[key])
            self.hashMap[key].val = value
        else:
            if len(self.hashMap) == self.capacity:
                last_node = self.tail.prev 
                self.remove_node(last_node)
                del self.hashMap[last_node.key]
            new_node = ListNode(key, value)
            self.hashMap[key] = new_node
        self.add_to_start(self.hashMap[key])            
        
