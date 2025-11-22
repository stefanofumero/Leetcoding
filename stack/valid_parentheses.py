"""
You are given a string s consisting of the following characters: '(', ')', '{', '}', '[' and ']'.
The input string s is valid if and only if:
Every open bracket is closed by the same type of close bracket. Open brackets are closed in the correct order.
Every close bracket has a corresponding open bracket of the same type. Return true if s is a valid string, and false otherwise.


Use a stack to put on the top every opening element you find in the array. When you find a closing element,
pop an element from the stack. If it's not belonging to the same family return false. If you get to the end
and the stack is empty, return true.

As a rule: WHEN YOU USE A DATA STRUCTURE, THINK ABOUT CASES WHERE IT CAN BE EMPTY AND YOU ARE TRYING TO ACCESS IT.  
This solution is O(n) in time and O(n) in space.
"""

class Solution:
    def isValid(self, s: str) -> bool:
        my_stack = []
        par : dict[str:str]= {
            '[':']',
            '{':'}',
            '(':')'
        }

        for c in s:
            if c in par:
                my_stack.append(c)
            else:
                if not my_stack: #pay attention to this edge case: closing bracket at the beginning and the stack is empty
                    return False
            
                prev_c = my_stack.pop()
                if c != par[prev_c]:
                    return False

        if len(my_stack)!=0:
            return False
        return True        