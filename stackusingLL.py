class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class Stack:
    def__init__(Self):
        self.top = None 
        self.length = 0
        
    
    def isEmpty(self):
        return (self.top == None)
    
    def push(self, data):
        temp = Node(data)
        temp.next = self.top
        self.top = temp
        self.length += 1

    def pop(self):
        if self.isEmpty():
            return "stack is empty"
        else:
            temp = self.top
            self.top = self.top.next
            self.length -= 1
            return temp.data
    def peek(self):
        if self.isEmpty():
            return "stack is empty"
        else:
            return self.top.data
        
    def size(self):
        return self.length
    
       