Deque is a type of data structure that has both functionalities of stack and queue. Deque stands for *Double Ended Queue* that means the data can be inserted and popped from so called *both ends*. We can solve these main functionalities efficiently under constant time complexity *O(1)*.  

## Real Life Examples:
- Palindrome checking: if both ends are identical then pop both of them. Otherwise return False as its no more a palindromic data
- Undo/Redo: The action taken by user is appended at the left side, simultaneously. Whenever, the user need to restore the action to its previous state then the action from the left side will be popped *(CTRL + Z)* and inserted to the right side for redo *(CTRL + Y)* functionality and vice versa.

## Implementation:

We can solve it in two ways. But I have attached the implementation of Circular Array as singly linked list is quite easy to code 👌 :
###### Circular Static Array:

Solving it using (CSA) is quite tricky. I have initialized front to the 1 and rear to the 0.
The Directions I am moving each of the pointers are the following:
	append_left <- (front will move to the left: decrement by 1)
	append_right -> (rear will move to the right: increment by 1)
	pop_left -> (rear will move to the right: increment by 1)
	pop_right <- (front will move to the left: decrement by 1)
	
You can visualize the implementation of these pointers which is., if our left pointer is 0. For further left insertions it will be wrapped around to the tail of the deque and insert the data from right to the left side. (Hint: Initially, our front pointer is at index 1 then it'll decrement the front pointer by 1, first then assigns the parametric data at the position 0 then it will be -1 (wrapped around to the tail), then it will be -2 that is the second last element of the deque and so forth). This is how I made an implementation of append_left member function in the direction of   right -> left. So is the case of append_right, and remaining functionalities. 
	
From this implementation my code will remain intact from any kind of throws/exceptions (IndexError) except for custom exceptions that I made. Above all, my code is robust and ready to beat any kind of desired test cases.
	
###### Circular Linked List:
Solving it using (CLL) is quite easy. Because we have to make a sentinel node and connect only the front node with it and tail nodes will be connected before the sentinel node as it'll be wrapped around due to its circular property. Remaining will be between front and tail node in a prompted order. 

## Implementation of Deque using Circular Array

```
class deque:

    def __init__(self, size = 10) -> None:

        self.data = [None] * size

        self.front, self.end = 1, 0

        self.len_ = 0

    def append_left(self, data):

        if not self.is_Full():

            self.front -= 1

            self.data[self.front] = data

        else:

            raise OverflowError ("Deque Is Full")

    def append_right(self, data):

        if not self.is_Full():

            self.end += 1

            if self.end < 0:

                self.data[self.end] = data

            else:

                self.data[self.end % len(self.data)] = data

        else:

            raise OverflowError ("Deque Is Full")

    def pop_left(self):

        if not self.is_Empty():

            if self.front >= 0:

                self.data[self.front % len(self.data)] = None

            else:

                self.data[self.front] = None

            self.front += 1

            if self.is_Empty():

                self.front, self.end = 1, 0

        else:

            raise OverflowError ("Deque Is Full")

    def pop_right(self):

        if not self.is_Empty():

            self.data[self.end] = None

            self.end -= 1

            if self.is_Empty():

                self.front, self.end = 1, 0

        else:

            raise OverflowError ("Deque Is Full")

    def is_Full(self):

        if self.front <= 0:

            return True if self.data[self.front - 1] != None else False

        return True if self.data[(self.front - 1) % len(self.data)] != None else False


    def is_Empty(self):

        if self.front <= 0:

            return True if self.data[self.front] == None else False

        return True if self.data[(self.front) % len(self.data)] == None else False

    def rotate(self):

        if not self.is_Empty():

            self.front, self.end = self.end, self.end - 1

        else:

            raise OverflowError ("Deque Is Full")

    def __str__(self):

        s = ""

        if not self.is_Empty():

            front = self.front

            if front >= len(self.data):

                front %= len(self.data)

            s = f"{self.data[front]} "

            temp, self.data[front] = self.data[front], "$"

            i = front + 1

            if i >= len(self.data):

                i %= len(self.data)

            while self.data[i] != "$":

                if self.data[i] is not None:

                    s += f"{self.data[i]} "

                i += 1

                if i >= len(self.data):

                    i %= len(self.data)

            self.data[front] = temp

        if not len(s): return "Deque: Empty"

        return "Deque: " + s

# Driver's Code

if __name__ == "__main__":

    dq = deque(3)

    dq.append_left(5)

    dq.append_left(3)

    dq.append_left(7)

    dq.pop_left()

    dq.rotate()

    print (dq)
    
```

*(Written By: Abdul Rehman Amer)*
