In this section, I have implemented a positional list through Doubly Linked List. 

## Positional List
A positional list is an Abstract Data Type that encapsulates the concept of ordered collection. We can use positional list more efficiently than any index-based or non index-based collection.

## Real Life Examples:
People in a queue in the act of waiting to buy tickets. But what if the following scenario got encountered:
- A person want to hang up before buying a ticket, this process *deletion in between*. Another case, person can add anyone in the queue after or before him, this process called *insertion in between*. 

## Approach:
I have implemented a positional linked list where each of the methods take `O(1)` time complexity because the user will give position of previous and next objects that they want to be inserted in between or getting discarded.

Please Look in the attached file where I've implemented this data structure.


You can give the CNICs of the people in this scenario. For example, I want to add between the CNIC # 32184-1846486-3 and 25879-1576120-4. The insert function will return the position of yours, CNIC, after inserted between them. 