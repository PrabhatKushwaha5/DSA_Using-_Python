class myQueue:
    def __init__(self, n):
        # Define Data Structures
        self.capacity = n
        self.n = []

    
    def isEmpty(self):
        # Check if queue is empty
        return len(self.n) == 0

    
    def isFull(self):
        # Check if queue is full
        return len(self.n) == self.capacity
    
    def enqueue(self, x):
        # Enqueue
        if not self.isFull():
            self.n.append(x)
        else:
            return "Queue Overflow"

    
    def dequeue(self):
        # Dequeue
        if self.isEmpty():
            return -1
        return self.n.pop(0)

    
    def getFront(self):
        # Get front element
        if self.isEmpty():
            return -1
        return self.n[0]
       
    
    def getRear(self):
        # Get rear element 
        if self.isEmpty():
            return -1
        return self.n[-1]
        
        
q = myQueue(5)
q.enqueue(10)
q.enqueue(20)
print(q.isEmpty())
print(q.isFull())
print(q.dequeue())
print(q.getFront())
print(q.getRear())
