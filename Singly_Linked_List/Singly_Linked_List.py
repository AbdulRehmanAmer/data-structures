# Implementing Singly Linked List as a Stack
# Since stack has only one component from which the data insert or remove, i.e., top of the stack, So We have "head" as a component of the stack and don't need the tail attribute because its not the property of stack to have a record of the data that was inserted at the very beginning.
class Singly_Linked_List:
    class Node:
        def __init__(self, data = None, next = None) -> None:
            self.data = data
            self.next = next
            
    def __init__(self) -> None:
        self.head = None
        self.size = 0
        
    def push(self, data):
        self.head = self.Node(data, self.head)
        self.size += 1

    def pop(self):
        if self.is_Empty(): raise "Linked List is Empty at the moment"
        node = self.head.next
        self.head.next = None
        self.head = node
        self.size -= 1
    
    def len(self):
        return self.size
        
    def is_Empty(self):
        return True if self.head == None else False    
    
    def __str__(self) -> str:
        s = "Singly Linked List: "
        
        if self.is_Empty(): return s + f"Empty"
        
        current_pointer = self.head
        while current_pointer != None:
            s += f"{current_pointer.data} "
            current_pointer = current_pointer.next
        
        return s
        

# Driver's Code   
if __name__ == "__main__":
    sll = Singly_Linked_List()
    sll.push(1)
    sll.push(2)
    sll.push(3)
    
    sll.pop()
    sll.pop()
    sll.pop()
    
    print (sll)