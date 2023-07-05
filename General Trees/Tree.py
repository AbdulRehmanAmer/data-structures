class Tree:
    class Node:
        def __init__(self, val = None) -> None:
            self.val = val
            self.children = list()
            
    def __init__(self) -> None:
        self.header = None
    
    def insert(self, val, parent = None):
        if parent == None:
            return self.add_Parent(val)
        parent.children.append(self.Node(val))
        return parent.children[-1] 
    
    def add_Parent(self, val):
        self.header = self.Node(val)
        return self.header
    
    def depth(self, parent = None):
        
        def func(root):
            if not root.children:
                return 0
            return 1 + max(func (c) for c in root.children)
        
        if parent == None:
            parent = self.header
        
        return func(parent)
    
if __name__ == "__main__":
    tree = Tree()
    refs = list()
    refs.append(tree.insert(1))
    refs.append(tree.insert(2, refs[0]))
    refs.append(tree.insert(3, refs[0]))
    refs.append(tree.insert(4, refs[0]))
    refs.append(tree.insert(5, refs[1]))
    refs.append(tree.insert(6, refs[1]))
    refs.append(tree.insert(7, refs[5]))
    refs.append(tree.insert(8, refs[6]))
    
    for x in refs:
        print ("Parent:", x.val, "Chilren:", [c.val for c in x.children])
        
    print (tree.depth(refs[5]))
        
    