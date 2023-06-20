from Array_Stack import *


def reverse_data(stack):
    reverse_stack = ArrayStack(stack.length())
    
    while stack.length() > 1:
        reverse_stack.push(stack.pop())
    
    return reverse_stack

# Driver's Code To get reverse_stack
if __name__ == "__main__":
    size = 3
    stack = ArrayStack(size)
    stack.push(1)
    stack.push(2)
    stack.push(3)
    
    stack_copy = stack.copy(size)
    reverse_stack = reverse_data(stack_copy)
    print ("Original Stack:", stack)
    print ("Reversed Stack:", reverse_stack)
    
     