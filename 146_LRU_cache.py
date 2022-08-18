class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        # linked list and hashmap
        self.capacity = capacity
        self.hashMap = {}
        self.LRU = Node(0,0)
        self.MRU = Node(0,0)

        self.LRU.next = self.MRU
        self.MRU.prev = self.LRU

    def remove(self, node):
        # remove the node from the linked list
        nodePrev = node.prev
        nodeNext = node.next

        nodePrev.next = nodeNext
        nodeNext.prev = nodePrev
        
    
    def insert(self, node):
        # insert to the MRU (tail of the linked list)
        tailNode = self.MRU.prev
        tailNode.next = node
        self.MRU.prev = node

        node.prev = tailNode
        node.next = self.MRU

    
    def get(self, key: int) -> int:
        # get the value of the key from hashmap
        if key in self.hashMap:
            # TODO:update the linked list
            node = self.hashMap[key]
            self.remove(node)
            self.insert(node)
            return node.value
        return -1
        

    def put(self, key: int, value: int) -> None:
        # key exist
        if key in self.hashMap:
            self.remove(self.hashMap[key])
        
        self.hashMap[key] = Node(key, value)
        self.insert(self.hashMap[key])

        # check the capacity
        if self.capacity < len(self.hashMap):
            # remove LRU cache
            lru = self.LRU.next
            self.remove(lru)
            del self.hashMap[lru.key]


        

# input: function calls and arguments
# output: result from the function calls

# constraints:
# get and put must be O(1)
# capacity >= 1
# value >= 0. key >= 0

# double link list and hashmap approach:
# use hashmap to achieve O(1) for the get function
# the key-value pair would be {key: linklist node}
# use the double linked list to implement the least recently used condition
# where the head of the linked list is the LRU 
# and the tail of the linked list is MRU

# TC: 
    # get: O(1)
    # put: O(1)
# SC:
    # O(C) + O(C)

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)