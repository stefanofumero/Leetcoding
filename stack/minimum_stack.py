"""
Design a stack class that supports the push, pop, top, and getMin operations.

MinStack() initializes the stack object.
void push(int val) pushes the element val onto the stack.
void pop() removes the element on the top of the stack.
int top() gets the top element of the stack.
int getMin() retrieves the minimum element in the stack.
Each function should run in O(1) time.


We use two stacks: one to keep track of all the elements, and another to keep track of the minimums.
"""


class MinStack:
    def __init__(self):
        self.my_stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        self.my_stack.append(val)
        val = min(val,self.min_stack[-1]) if self.min_stack else val
        self.min_stack.append(val)
        
    def pop(self) -> None:
        self.my_stack.pop()
        self.min_stack.pop()

    def top(self) -> int:
        return self.my_stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]
