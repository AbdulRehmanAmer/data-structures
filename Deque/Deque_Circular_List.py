# Implementing Deque using circular static Array
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
    