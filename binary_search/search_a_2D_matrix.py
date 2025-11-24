"""
You are given an m x n 2-D integer array matrix and an integer target.
Each row in matrix is sorted in non-decreasing order.
The first integer of every row is greater than the last integer of the previous row.
Return true if target exists within matrix or false otherwise.
Can you write a solution that runs in O(log(m * n)) time?


Pretty simple and straightforward binary search application. Pay attention to write clean code and to name variables properly.
"""

from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        """
        Apply binary search first to the rows, then to columns

        let's imagine you have n rows and m columns:
        it's log(m) to find the correct row, while it is log(n)
        to find the correct column. Thus, in total, it's
        log(m) + log(n), which is the same as log(n*m).
        """
        l,r = 0,len(matrix)-1
        found_row = False

        while l <= r:
            m = (l+r)//2
            a1,an = matrix[m][0],matrix[m][len(matrix[m])-1]

            if target >= a1 and target <= an:
                found_row = True
                break
            elif target >= an:
                l = m+1
            else:
                r = m-1
        
        if not found_row:
            return False
        
        f = m
        l,r = 0, len(matrix[0])

        while l <= r:
            m = (l+r)//2
            val = matrix[f][m]
            if val == target:
                return True
            elif val >= target:
                r = m-1
            else:
                l = m+1
        
        return False