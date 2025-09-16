class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0
    
    def enqueue(self,item):
        self.items.append(item)

    def dequeue(self):
        if len(self.items) == 0:
            print("Empty")
            return
        x = self.items.pop(0)
        return x
    
    def front(self):
        if len(self.items) == 0:
            print("Empty")
            return
        return self.items[0]
    
    def rear(self):
        if len(self.items) == 0:
            print("cannot read")
        
        return self.items[-1]
    def size(self):
        return len(self.items)
    



queue = Queue()
print(queue.is_empty())
queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)
queue.enqueue(40)
print(queue.dequeue())
print(queue.front())
print(queue.rear())
print(queue.size())