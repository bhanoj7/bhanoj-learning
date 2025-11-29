class queue:
    def __init__(self):
        self.queue=[]
    def enqueue(self,x):
        return self.queue.append(x)
    def dequeue(self):
        return self.queue.pop(0)
    def peek(self):
        return self.queue[0]
    def is_empty(self):
        if self.queue:
            return False
        else:
            return True
    def size(self):
        return len(self.queue)
