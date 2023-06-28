class Circular_Linked_Queue:
    
    class Node:
        def __init__(self, data = None, next = None) -> None:
            self.data = data
            self.next = next
            
    def __init__(self) -> None:
        self.tail = None
        self.size = 0
    
    def enqueue(self, data):
        if self.is_Empty(): 
            self.tail = self.Node(data, self.tail)
            self.tail.next = self.tail
        else:
            new_node = self.Node(data, self.tail.next)
            self.tail.next = new_node
            self.tail = new_node
            
        self.size += 1
    
    def dequeue(self):
        if self.is_Empty(): raise "Empty Circular Linked List"
        if self.size == 1:
            self.tail = None
        else:
            to_remove = self.tail.next
            self.tail.next = to_remove.next
            del to_remove
            
        self.size -= 1
            
    def is_Empty(self):
        return True if self.tail == None else False
    
    def __len__(self): return self.size
    
    def rotate(self):
        if self.is_Empty(): raise "Empty Circular Linked List"
        
        self.tail = self.tail.next
    
    def __str__(self) -> str:
        s = "Circular Linked Queue: "
        if self.is_Empty(): return s + "Empty"
        
        current_pointer = self.tail.next
        temp, current_pointer.data = current_pointer.data, "$"# $ is a sentinel value
        s += f"{temp} "
        current_pointer = current_pointer.next
        while  current_pointer.data != "$":
            s += f"{current_pointer.data} "
            current_pointer = current_pointer.next
        
        self.tail.next.data = temp# restoring its data
        
        return s
        
if __name__ == "__main__":
    queue = Circular_Linked_Queue()
    
    queue.enqueue("A")
    queue.enqueue("B")
    queue.enqueue("C")
    queue.enqueue("D")
    queue.enqueue("E")
    queue.enqueue("F")
    queue.enqueue("G")
    
    queue.dequeue()
    
    # queue.rotate()
    queue.rotate()
    
    print (queue)