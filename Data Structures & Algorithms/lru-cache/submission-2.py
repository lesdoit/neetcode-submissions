class Node:
    def __init__(self, key: int = -1, val: int = -1, next: Node = None, prev: Node = None):
        self.key = key
        self.val = val
        self.next = next 
        self.prev = prev

class LRUCache:

    def __init__(self, capacity: int):
        self.mp = {}
        self.cap = capacity
        self.head, self.tail = Node(), Node()
        self.head.next = self.tail
        self.tail.prev = self.head
        
    def touch(self, node: Node) -> None:
        if node.prev:
            node.prev.next = node.next
        if node.next:
            node.next.prev = node.prev
        
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node 
        node.prev = self.head

    
    def remove(self) -> None: 
        target = self.tail.prev
        target.prev.next = target.next
        self.tail.prev = target.prev
        target.next = target.prev = None
        del self.mp[target.key]


    def get(self, key: int) -> int:
        if key in self.mp:
            self.touch(self.mp[key])
            return self.mp[key].val
        else: 
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.mp:
            self.mp[key].val = value
            self.touch(self.mp[key])
        else:
            
            # case 1 - not enough space 
            if len(self.mp) == self.cap:
                self.remove()
            
            # case 2 - enough space 
            node = Node(key, value)
            self.touch(node)
            self.mp[key] = node
            
