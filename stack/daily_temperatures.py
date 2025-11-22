"""
You are given an array of integers temperatures where temperatures[i] represents the daily temperatures on the ith day.
Return an array result where result[i] is the number of days after the ith day before a warmer temperature appears on a
future day. If there is no day in the future where a warmer temperature will appear for the ith day, set result[i] to 0 
instead.

DP solution:
start from the penultimate element (the last is 0 for sure)
if the penultimate > last, it's zero, otherwise 1
move to the left with a pointer i, then check i+1:
- el[i+1] > el[i] -> res [i] = 1
- Otherwise, check at position i + el[i] till el[i] != 0


You can also use a stack to keep track of the indices of the days with unresolved warmer temperatures.
Store on a stack pairs [temp,index]. For each new temperature, pop from the stack while the current temperature is higher than
the temperature at the index stored at the top of the stack, otherwise append the current temperature and index to the stack.
"""
from typing import List

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        n_days = len(temperatures)
        res = [0]*n_days

        for i in range(n_days-2,-1,-1):
            if temperatures[i+1] > temperatures[i]:
                res[i] = 1
                continue
            j = i+1
            days = 0
            while res[j] != 0: 
                j += res[j] 
            
                if j >= n_days:
                    res[i] = 0 
                    break
                if temperatures[j] > temperatures[i]:
                    res[i] = j - i  
                    break

        return res
            