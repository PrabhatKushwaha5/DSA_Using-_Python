class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0
    
    def push(self,item):
        self.items.append(item)

    def pop(self):
        if len(self.items) == 0:
            return "Cannot pop"
        x = self.items.pop()
        return x
    
    def top(self):
        if len(self.items) == 0:
            return "CanNot top"
        return self.items[-1]
    
    def size(self):
        return len(self.items)
    


stack = Stack()
print(stack.is_empty())
stack.push(10)
stack.push(20)
stack.push(30)
print(stack.pop())
print(stack.top())
print(stack.size())