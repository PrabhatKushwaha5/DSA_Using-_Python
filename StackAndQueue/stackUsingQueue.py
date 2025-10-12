class MyStack(object):
    def __init__(self):
        self.stack = []

    def push(self, x):
        self.stack.append(x)

    def pop(self):
        return self.stack.pop() if self.stack else None

    def top(self):
        return self.stack[-1] if self.stack else None

    def empty(self):
        return len(self.stack) == 0



if __name__ == "__main__":
    obj = MyStack()
    obj.push(10)
    obj.push(20)
    obj.push(30)
    print("Top element:", obj.top())    
    print("Popped element:", obj.pop())  
    print("Top element:", obj.top())     
    print("Is empty:", obj.empty())      
    obj.pop()
    obj.pop()
    print("Is empty after popping all:", obj.empty())  
