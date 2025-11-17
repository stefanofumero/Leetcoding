"""
You are given an integer array heights where heights[i] represents the height of the ith bar.
You may choose any two bars to form a container. Return the maximum amount of water a container can store.

Starting with a wall in position 0 and the other in position n. We keep the maximum that we found so far, 
by multiplying the min among the height of the two walls by their distance (width). Which wall to move in the 
next iteration? I would keep fixed the highest one and move the other, so that we can look for improvements
"""
from typing import List

class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l,r = 0,len(heights) -1 
        res = 0

        while l < r:
            h = min(heights[l],heights[r])
            w = r - l 
            res = max(res,h*w)
            #Pay attention, move the lowest one
            if heights[l] <= heights[r]:
                l += 1
            else:
                r -= 1

        return res