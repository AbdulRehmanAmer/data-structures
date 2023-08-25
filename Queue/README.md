After covering the chapter of stack, next data structure is Queue. I bet that you have somehow engaged yourself in this data structure in real life examples.

## Queue:
Queue is a data structure that follows the principle of first-in, first-out that means the data inserted (enqueued in the queue) will be popped (dequeued from the queue) first then remaining data would get their turn. 
-	There are two main mechanism this data structure has i.e., enqueue and dequeue as elaborated above.
-	Also, people call it a close cousing of stack, as a funny term.

## Real Life Examples:
- Buying ticket from a cinema house, where each person that arrives first would get their turn first.
- Phone calls in a customer care center. Call center hold that phone call unless and until every calls will be dequeued that were enqueued before it.

As told earlier in the stack segment, https://github.com/AbdulRehmanAmer/data-structures/blob/master/Stack/Stack.md, python does not have array data structure but we have list (dynamic array) that we can use it as a adapter design pattern to implement our requirement. To implement queue in an array structure, obviously, we should have size as a parameter or to make our code more robust, we can create a default parameter of size in constructor. 


## Implementation of Queue using Static Array:
```

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
```
 
 *(Written By: Abdul Rehman Amer)*
