"""
You are given an array of strings tokens that represents a valid arithmetic expression in Reverse Polish Notation.
Return the integer that represents the evaluation of the expression.
The operands may be integers or the results of other operations.
The operators include '+', '-', '*', and '/'.
Assume that division between integers always truncates toward zero.

here we can use a stack: read the vector forward, when you find a number, push it into the stack. When you find
an op., pop the last two number appended and execute the op. The result has to be appended back again within the stack.
At the end, the result is the stack[-1].


PAY ATTENTION TO THE DIFFERENT OP ON STACKS AND QUEUES.
"""

from typing import List

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        if not tokens:
            return 0

        values = []

        for t in tokens:
            if t not in ['+','-','*','/']:
                values.append(int(t))
            else:
                res = 0
                val2 = values.pop()
                val1 = values.pop()
                if t == '+':
                    res = val1 + val2
                elif t == '-':
                    res = val1 - val2
                elif t == '*':
                    res = val1 * val2
                else:
                    res = int(val1/val2)
                values.append(res)

        return values[-1]
    


"""
Here it is interesting also the recursive solution:
"""
def evalRPN_recursive(tokens: List[str]) -> int:

    def helper(tokens: List[str]) -> int:
        t = tokens.pop()
        if t not in ['+','-','*','/']:
            return int(t)
        else:
            val2 = helper(tokens)
            val1 = helper(tokens)
            if t == '+':
                return val1 + val2
            elif t == '-':
                return val1 - val2
            elif t == '*':
                return val1 * val2
            else:
                return int(val1/val2)

    return helper(tokens)