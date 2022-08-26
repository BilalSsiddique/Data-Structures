
# Queue work on the first in first out concept.
# Example : A line of people waiting to buy a ticket at a cinema hall.A new person will 
# join the line from the end and the person standing at the front will be
# the first to get the ticket and leave the line.
from collections import deque
class Queue:
    def __init__(self):
        # create/initialize a Queue
        self.queue= deque()

    def enqueue(self,val):
        # Append (left side) of the queue
        self.queue.appendleft(val)
    def dequeue(self):
        # remove and return the first value 
        return self.queue.pop()
    def is_empty(self):
        # return True if queue is empty else false
        return len(self.queue)==0
    def size(self):
        # return length of items in the queue
        return len(self.queue)
    
# initialize object
qu= Queue()
# check empty
print(f"Is_Empty: {qu.is_empty()}")
for i in range(5):
    print(f"Pushing {i} in the Queue")
    qu.enqueue(i)
#length of Queue
print("Length of Queue is :",qu.size())
# Pop
print(f"Remove {qu.dequeue()} from the Queue")
#length of Queue
print("Length of Queue is now:",qu.size()) 
# Queue
print("Whole Queue :",qu.queue)
# check empty
print(f"Is_Empty: {qu.is_empty()}")
