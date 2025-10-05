#LRU cache - least recently used
class Node:
    def __init__(self,val):
        self.val=val
        self.next=None
        self.prev=None
    
class LRUcache:
    
    def __init__(self, cap):
        self.head=Node(0)
        self.tail=Node(0)
        self.head.next=self.tail
        self.tail.prev=self.head
        self.cap=cap
        self.count=0
        
        
    def removetail(self):
        prev=self.tail.prev.prev
        prev.next=self.tail
        
        
        
        
    def addnode(self, val):
        if self.count==self.cap:
            self.removetail()
            self.count-=1
        node=Node(val)
        nex=self.head.next
        nex.prev=node
        self.head.next=node
        node.next=nex
        self.count+=1
    
    def getLRU(self):
        return self.head.next
    
    def removenode(self, node):
        cur=self.head
        while cur!=node:
            cur=cur.next
        cur.prev.next=cur.next
            
            
             
        
lru = LRUcache(5)

lru.addnode(3)
lru.addnode(6)
lru.addnode(4)
lru.addnode(7)
lru.addnode(9)
lru.addnode(66)


print(lru.getLRU().val)
