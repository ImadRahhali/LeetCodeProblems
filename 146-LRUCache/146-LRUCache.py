# Last updated: 6/11/2025, 10:14:24 PM
class Node:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.prev = self.next = None
class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {} #map key to a node of key-value

        self.left = Node(0,0) #points to the LRU
        self.right = Node(0,0) #points to the MRU

        self.left.next = self.right
        self.right.prev = self.left
    
    def insert(self,node): # insert it at Right so its the MRU
        prv, nxt = self.right.prev, self.right
        prv.next = nxt.prev = node
        node.prev, node.next = prv, nxt
    
    def remove(self,node): # remove a middle node
        prv, nxt = node.prev, node.next # take the prev, next of that node since its on middle
        prv.next, nxt.prev = nxt, prv #update them
    
    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key]) # this makes it the MRU
            return self.cache[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])

        if len(self.cache) > self.cap:
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]
        
