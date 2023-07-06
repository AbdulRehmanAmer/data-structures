Circular Linked Queue contains one attribute which points back to the front of the queue. We can also call it a *Never Ending Queue* as it dynamically fill the queue with the data and extend its length. 

### Why not to use Circular Array Queue instead of Circular Linked Queue
In the section of singly linked list, I have explained in a detailed theoretical and practical format that why we approach towards linked list. Here we are using circular linked queue instead of circular array queue, because: 
Circular array queue is not space efficient, the reason being, array has a static size and empty cells, allocated with it, that will be filled by upcoming prompted data. In this case, it might be possible that the empty cell won't be filled because user's task is fulfilled before reaching to the array limit, that leads to the inefficiency of memory. In this scenario, a dynamic sized-queue is required that fulfills the user's requirement and don't waste any space in the memory.
- There are two dynamic-sized data structure approach:
- List
- Circular Linked Queue

Python List is not efficient when it comes to the time analysis, because queue has a property that data is enqueued from the backward and dequeued from the front. In the case of dequeue, we use pop(0) in python list and it takes *O(N)* because all cells ,Infront of it, will be shift to the left side one by one.

Another efficient case, we can create our own custom data structure using Circular Linked List, named as Circular Linked Queue, in which tail will be shift rightward and assign to the newest enqueued data that takes *O(1)* and it dequeue the data as it wraped around to the first element of the queue and the following command will be executed in constant time *O(1)* i.e.,

**Attached An Image for better understanding**
```
old = self.tail.next # this is the first element that was enqueued in the queue
self.tail.next = old.next
del old
```
![image](https://github.com/AbdulRehmanAmer/data-structures/assets/115944146/07a8ff1a-18fc-4f1b-864f-1ff6eec770b4)

