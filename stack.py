from collections import deque
class stack:
    def __init__(self):
        # create a stack
        self.container= deque()

    def push(self,val):
        # append(always right side) value to the stack
        self.container.append(val)
    def remove(self):
        # remove and return the last value 
        return self.container.pop()
    def peek(self):
        # return top/last value from the stack
        return self.container[-1]
    def is_empty(self):
        # return True if stack is empty else false
        return len(self.container)==0
    def size(self):
        # return length of items in the stack
        return len(self.container)
    
# initialize object
st= stack()
for i in range(5):
    print(f"Pushing {i} in the stack")
    st.push(i)
#length of stack
print("Length of stack is :",st.size())
# Pop
print(f"Remove {st.remove()} from the stack")
#length of stack
print("Length of stack is now:",st.size()) 
# Top value
print("Stack top value is :",st.peek())
# Stack
print("Whole stack :",st.container)