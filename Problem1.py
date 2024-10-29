#146 LRU CACHE
class LRUCache(object):  #T.C -> O(1) , S.C->O(1)

    class Node:
        def __init__(self,key,val):
            self.key = key
            self.val = val
            self.prev = None
            self.next = None

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.head = self.Node(-1,-1)
        self.tail = self.Node(-1,-1)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.hash_map = {}
    
    def removeNode(self,curr):
        curr.prev.next = curr.next
        curr.next.prev = curr.prev
    def moveToHead(self,curr):
        curr.next = self.head.next
        curr.prev = self.head
        curr.next.prev = curr
        self.head.next = curr

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.hash_map:
            curr = self.hash_map[key]
            self.removeNode(curr)
            self.moveToHead(curr)
            return self.hash_map[key].val
        else:
            return -1
        
        

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if key in self.hash_map:
            curr = self.hash_map[key]
            curr.val = value
            self.removeNode(curr)
            self.moveToHead(curr)
        else:
            if len(self.hash_map) == self.capacity:
                tailPrev = self.tail.prev
                self.removeNode(tailPrev)
                if tailPrev.key in self.hash_map:
                    del self.hash_map[tailPrev.key]
                
            node = self.Node(key,value)
            self.moveToHead(node)
            self.hash_map[key] = node

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)