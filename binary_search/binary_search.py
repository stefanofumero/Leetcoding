"""
You are given an array of distinct integers nums, sorted in ascending order, and an integer target.
Implement a function to search for target within nums. If it exists, then return its index, otherwise, return -1.
Your solution must run in O(logn) time.

Simple binary search implementation. Don't forget, when updating l and r, to set them to m+1 or m-1 to avoid infinite loops!!!!
"""
from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l,r = 0,len(nums)-1
        while l <= r:
            m = (l+r)//2
            val = nums[m]
            if val == target:
                return m
            elif val < target:
                l = m+1
            else:
                r = m-1
        return -1