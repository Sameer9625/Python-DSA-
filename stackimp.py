class stack:
    def__init__(self):
    self.top = []

    def push(self,data):
        self.top.append(data)
        
    def pop(self):
        if len(self.top) == 0:
            return "stack is empty"
        else:
            return self.top.pop()
    def peek(self):
        if len(self.top) == 0:
            return "stack is empty"
        else:
            return self.top[-1]
    def size(self):        
        return len(self.top)
    def isEmpty(self):       
        return len(self.top) == 0 
s = stack()
s.push(1)
s.push(2)   
print(s.peek())    # Output: 2
print(s.pop())     # Output: 2
print(s.size())    # Output: 1
print(s.isEmpty()) # Output: False
