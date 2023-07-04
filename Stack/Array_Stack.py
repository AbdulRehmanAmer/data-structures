#Stack Implementation using cpp array (static sized array)
class ArrayStack:
    def __init__(self, size):
        self.data = ["$"] * size
        self.size = 0
    
    def push(self, data):
        if not self.is_Full():
            self.data[self.size] = data
            self.size += 1
        else:
            raise "Stack is Full"
    
    def pop(self):
        if not self.is_Empty():
            temp = self.data[self.size - 1]
            self.data[self.size - 1] = "$"
            self.size -= 1
            return temp
        else:
            raise "Stack is Empty"
    
    def peek(self):
        if not self.is_Empty():
            return self.data[self.size - 1]
        raise ("Stack is Empty")
            
    def length(self):
        return self.size + 1
    
    def is_Full(self):
        return True if self.size == len(self.data) else False

    def is_Empty(self):
        return True if self.size == 0 else False

    def copy(self, size):
        stack = ArrayStack(size)
        for i in range(self.size):
            stack.push(self.data[i])
        
        return stack
    
    def __str__(self) -> str:
        s = ""
        for i in range(self.size):
            s += f"{self.data[i]} "
        s += "\n"
        return s
    
# Driver's Code for stack practicality
if __name__ == "__main__":
    stack = ArrayStack(3)
    stack.push(1)
    stack.push(2)
    stack.push(3)
    
    print ("Length of Stack:",stack.length())
    print ("Popping from the stack:", stack.pop())
    print ("Peek data of the stack:", stack.peek())
    print ("Stack is Full:", stack.is_Full())
    print ("Stack is Empty:", stack.is_Empty())
    
    