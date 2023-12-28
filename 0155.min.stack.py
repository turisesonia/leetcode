"""
# 155
Medium
Min Stack

https://leetcode.com/problems/min-stack

Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

Implement the MinStack class:
* MinStack() initializes the stack object.
* void push(int val) pushes the element val onto the stack.
* void pop() removes the element on the top of the stack.
* int top() gets the top element of the stack.
* int getMin() retrieves the minimum element in the stack.

You must implement a solution with O(1) time complexity for each function.

Example 1:
Input
["MinStack","push","push","push","getMin","pop","top","getMin"]
[[],[-2],[0],[-3],[],[],[],[]]

Output
[null,null,null,null,-3,null,0,-2]

Explanation
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin(); // return -3
minStack.pop();
minStack.top();    // return 0
minStack.getMin(); // return -2

Constraints:
* -2^31 <= val <= 2^31 - 1
* Methods pop, top and getMin operations will always be called on non-empty stacks.
* At most 3 * 104 calls will be made to push, pop, top, and getMin.
"""


class MinStack:
    def __init__(self):
        self.stack = []
        # ! Consider each node in the stack having a minimum value. (Credits to @aakarshmadhavan)
        self.min = []

    def push(self, val: int) -> None:
        if not self.min:
            self.min.append(val)
        else:
            min_ = min(self.min[-1], val)
            self.min.append(min_)

        self.stack.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.min.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min[-1]


if __name__ == "__main__":
    # * Test case 1
    # min_stack = MinStack()
    # min_stack.push(-2)
    # min_stack.push(0)
    # min_stack.push(-3)
    # assert min_stack.getMin() == -3
    # min_stack.pop()
    # assert min_stack.top() == 0
    # assert min_stack.getMin() == -2

    # * Test case 2
    # min_stack = MinStack()
    # min_stack.push(0)
    # min_stack.push(1)
    # min_stack.push(0)
    # assert min_stack.getMin() == 0
    # min_stack.pop()
    # assert min_stack.getMin() == 0

    # # * Test case 3
    min_stack = MinStack()
    min_stack.push(512)
    min_stack.push(-1024)
    min_stack.push(-1024)
    min_stack.push(512)
    min_stack.pop()
    assert min_stack.getMin() == -1024
    min_stack.pop()
    assert min_stack.getMin() == -1024
    min_stack.pop()
    assert min_stack.getMin() == 512
