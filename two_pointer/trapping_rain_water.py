"""
You are given an array of non-negative integers height which represent an elevation map. Each value height[i] 
represents the height of a bar, which has a width of 1.
Return the maximum area of water that can be trapped between the bars.

The rain that can be trapped is computed, at each position, by knowing the highest wall on the left and the highest
on the right.
We can keep those two info in two different arrays: One contains the highest on the left, the other the highest
on the right. This solution is actually O(n) space and time. There's an optimization that allows us to reduce space 
complexity to O(1).

We can use a double pointer strategy: one at the beginning, the other at the end. Basically, we need to move the 
one which is lower, because that is our bottlenck, we don't actually need to know the maximum from the other side
if we moved the smallest
"""
from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        l,r = 0,len(height) - 1
        res = 0
        maxL,maxR = 0,0
        while l < r:
            if maxL <= maxR:
                l += 1
                maxL = max(maxL,height[l])
                res += maxL - height[l]
            else:
                r -= 1
                maxR = max(maxR,height[r])
                res += maxR - height[r]