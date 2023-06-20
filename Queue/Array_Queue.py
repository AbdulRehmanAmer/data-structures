# Queue Implementation using Circular List
class ArrayQueue:
    def __init__(self, size = 10) -> None:
        self.data = [None] * size
        self.size = 0
        self.front = 0
        
    def enqueue(self, data):
        if not self.is_Full():
            self.data[self.size % len(self.data)] = data
            self.size += 1
        else:
            raise IndexError
        
    def dequeue(self):
        if not self.is_Empty():
            self.data[self.front % len(self.data)] = None
            self.front += 1
            
            if self.front == self.size:
                self.front, self.size = 0, 0
        else:
            raise "Queue is Empty"
        
    def get_front(self):
        if not self.is_Empty():
            return self.data[self.front]  
        else:
            raise "Queue is Empty"
    
    def is_Empty(self):
        return True if self.size == 0 else False

    def is_Full(self):
        return True if self.data[self.size % len(self.data)] != None else False


    def resize(self, size):
        track = self.data[ : ]
        self.data = [None] * size
        
        resize_queue_size = 0
        
        for i in range(self.front, self.size):
            self.data[resize_queue_size] = track[i % len(track)]
            resize_queue_size += 1
        
        self.front, self.size = 0, resize_queue_size
            
    def __str__(self) -> str:
        s = "Queue: "
        for i in range(self.front, self.size):
            s += str(self.data[i % len(self.data)]) + " "
            
        if s == "Queue: ": s += "Empty"
        return s 
    
# Driver's Code
if __name__ == "__main__":
    queue = ArrayQueue(7)
    
    queue.enqueue("A")
    queue.enqueue("B")
    queue.enqueue("C")
    queue.enqueue("E")
    queue.enqueue("F")
    queue.enqueue("G")
    queue.enqueue("H")
    
    queue.dequeue()
    queue.dequeue()
    queue.dequeue()
    
    queue.enqueue("I")
    queue.enqueue("J")
    queue.enqueue("K")
    
    queue.resize(13)
    print (queue)

    