from stack import stack
from queue import queue

s=stack()

# push items
s.push(1)
s.push(2)
s.push(3)

# print size
print(s.size())
# print peek
print(s.peek())
# print pop
print(s.pop())
# print is_empty
print(s.is_empty())


# create object
q=queue()
# enqueue items
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
# print size
print(q.size())
# print peek
print(q.peek())
# print deq
print(q.dequeue())
# print is_empty
print(q.is_empty())

#Example Output
# 3
# 3
# 3
# False
# 3
# 1
# 1
# False