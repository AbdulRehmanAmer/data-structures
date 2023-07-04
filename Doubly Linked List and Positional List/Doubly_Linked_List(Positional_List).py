class Doubly_Linked_List:
    
    class Node:
        def __init__(self, val = None, prev = None, next = None) -> None:
            self.val = val
            self.prev, self.next = prev, next
            
    def __init__(self) -> None:
        self.__header, self.__trailer = self.Node(), self.Node()
        self.__header.next, self.__trailer.prev = self.__trailer, self.__header
        self.__size = 0
        
        self.alpha = 97
        self.__references = {
            "Header": self.__header,
            "Trailer": self.__trailer
                             }
        self.__references_rev_map = {
            self.__header : "Header",
            self.__trailer : "Trailer"
        }
        
    def insert_first(self, val):
        reference = self.insert_between(val, self.__references_rev_map[self.__header], self.__references_rev_map[self.__header.next])
        return reference

    def insert_last(self, val):
        reference = self.insert_between(val, self.__references_rev_map[self.__trailer.prev], self.__references_rev_map[self.__trailer])
        return reference
    
    def insert_between(self, val, predecessor, successor):
        node = self.Node(val, self.__references[predecessor], self.__references[successor])
        self.__references[predecessor].next, self.__references[successor].prev = node, node
        self.__size += 1
        self.__references[chr(self.alpha)] = node        
        self.__references_rev_map[node] = chr(self.alpha)
        self.alpha += 1
        
        return chr(self.alpha - 1)

    def delete_between(self, node):
        if self.__references[node] is not None:
            self.__references[node].prev.next, self.__references[node].next.prev = self.__references[node].next, self.__references[node].prev
            
            self.__references_rev_map[self.__references[node]] = None
            self.__references[node] = None
            self.__size -= 1
        else:
            raise "This node does not exist"
    
    def delete_first(self):
        if self.empty(): raise "Empty Linked List"
        self.delete_between(self.__references_rev_map[self.__header.next])
    
    def delete_last(self):
        if self.empty(): raise "Empty Linked List"
        self.delete_between(self.__references_rev_map[self.__trailer.prev])
        
    def empty(self):
        return True if not self.__size else False
    
    def __str__(self):
        s = "Doubly Linked List: "
        for x in self:
            s += f"{x} "
        
        return s if not self.empty() else s + "Empty"
    
    def __iter__(self):
        self.current_pointer = self.__header.next
        return self

    def __next__(self):
        if self.current_pointer.val != None:
            get_val = self.current_pointer.val
            self.current_pointer = self.current_pointer.next
            return get_val
        raise StopIteration
    
    def get_val(self, ref):
        try:
            return self.__references[ref].val
        except: raise "No such node exists"
        
# Driver's Code
if __name__ == "__main__":
    dll = Doubly_Linked_List()
    refs = []
    refs.append(dll.insert_first(1))
    refs.append(dll.insert_last(2))
    refs.append(dll.insert_last(3))
    refs.append(dll.insert_first(0))
    
    refs.append(dll.insert_between(1.5, refs[0], refs[1]))
    
    print (dll)
    print (dll.get_val(refs[4]))
    
    dll.delete_first()
    dll.delete_last()
    dll.delete_between(refs[4])
    print (dll)
    dll.delete_between(refs[4])
    
    print (refs)