class HeapNode:
    def __init__(self, node, val):
        self.node = node
        self.val = val 
    
    def __lt__(self, other):
        return self.val < other.val

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        min_heap = []

        for head in lists:
            if head:
                heapq.heappush(min_heap, HeapNode(head, head.val))
        
        dummy = ListNode()
        cur = dummy
        while min_heap:
            min_node = heapq.heappop(min_heap)
            min_node = min_node.node
            if min_node.next:
                heapq.heappush(min_heap, HeapNode(min_node.next, min_node.next.val))
            cur.next = min_node
            cur = cur.next 
        return dummy.next 