class LRUCache:
    class DoublyLinkedList:
        def __init__(self, data = None, key = None):
            self.data = data
            self.key = key
            self.prev, self.next = None, None

    def __init__(self, capacity: int):
        self.capacity = capacity
        
        self.head = self.DoublyLinkedList()
        self.tail = self.DoublyLinkedList()
        self.head.next = self.tail
        self.tail.prev = self.head
        
        self.hashtable = dict()

    def __move_to_end(self, key):
            # Isolating getter DoublyLinkedList
            self.hashtable[key].prev.next = self.hashtable[key].next
            self.hashtable[key].next.prev = self.hashtable[key].prev

            # Maintaining the reference of getter DoublyLinkedList
            self.hashtable[key].prev = self.tail.prev
            self.tail.prev.next = self.hashtable[key]
            self.hashtable[key].next = self.tail
            self.tail.prev = self.hashtable[key]
            
    def get(self, key):
        if key in self.hashtable:
            if self.hashtable[key] is None: return -1 # Key was existing but it got evicted.
            self.__move_to_end(key)
            return self.hashtable[key].data
        return -1 # If key does not exist

    def put(self, key: int, value: int) -> None:
        # Connecting the links of current node with the tail to make it (recently most used node)
        if key in self.hashtable and self.hashtable[key] is not None: 
            self.hashtable[key].data = value
            self.__move_to_end(key)
            
        else:
            if self.capacity:
                node = self.DoublyLinkedList(value)
                node.key = key
                self.hashtable[key] = node
                self.tail.prev.next = node
                node.prev = self.tail.prev

                self.tail.prev = node
                node.next = self.tail
                
                self.capacity -= 1
                
            elif not self.capacity: # Removing the least used cache in order to add new node
                self.hashtable[self.head.next.key] = None
                self.head.next.data = value
                self.head.next.key = key
                self.hashtable[key] = self.head.next
                
                self.__move_to_end(key)