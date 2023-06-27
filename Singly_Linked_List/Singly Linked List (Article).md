A Singly Linked List is a linear collection of nodes where each node connects to the other using its reference . Unlike array as it stores in the memory in a contiguous portion, It stores each node in the memory randomly and we can access these nodes by its reference/address.

### Why using it instead of Array?
We use Singly Linked List (SLL) when we don't have a large space of **contiguous** memory portion. Machine stores the memory of an array in a contiguous portion and it is not guaranteed from which memory portion of an array will be occupied. 

	For example, we have 10 blocks of memory, *just an example*, and we need 5 blocks to occupied for our required array. It depends on the machine which 5 blocks of the memory it will choose. It can start from 2nd block or from the 5th block, etc. 
	So, let's say we have all contiguous blocks occupied and we have few random blocks left in the memory such as *2nd, 3rd, 5th, 7th and 10th* block. We can see this is not the contiguous segment to store the array. 
	Here SLL takes a heroic step and 5 remaining block can be filled with a node as it stores randomly in the memory, as told in the above section. We can make our custom order of the node by storing the reference of the other node.

### Real Life Examples:
	Bus stops: Each node contains the information of the next stop 
	Web Browser History: Where each node contains the information of previously visited site and vice versa. It can contain the refernce of recent site where recent site points to its parent site and so forth. It is possible, as an initial state, that current node might not have any reference of any site (previous or the next from where current site got browsed).

### Implementation of Singly Linked List Using Stack:
```
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
    
```