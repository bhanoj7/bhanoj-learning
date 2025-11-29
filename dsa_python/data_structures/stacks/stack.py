class stack:
    def __init__(self):
        self.stack=[]
    def push(self,x):
        return self.stack.append(x)
    def pop(self):
        return self.stack.pop()
    def peek(self):
        return self.stack[-1]
    def is_empty(self):
        if self.stack:
            return False
        else:
            return True
    def size(self):
        return len(self.stack)
