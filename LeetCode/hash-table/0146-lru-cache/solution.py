class Node:
    def __init__(self,key,val):
        self.key,self.val=key,val
        self.next,self.prev=None,None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity=capacity
        
        #Intializing a Doubly linked list and with left for LRU and right for MRU
        self.left,self.right=Node(0,0),Node(0,0)
        self.left.next,self.right.prev=self.right,self.left

        #Intializing a dictionary because we need to store key and nodes to access in O(1)
        self.cache={}
    
    def remove(self,node:Node): # Removes the node from any place
        node.prev.next,node.next.prev=node.next,node.prev

    def insert(self,node:Node): # Appends the node to the right 
        prev,nxt=self.right.prev,self.right
        prev.next=nxt.prev=node
        node.next,node.prev=nxt,prev


    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1


    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key]=Node(key,value)
        self.insert(self.cache[key])

        if len(self.cache)>self.capacity:
            #Here we will remove and delete the LRU from cache and also list
            lru=self.left.next
            self.remove(lru)
            del self.cache[lru.key]


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
