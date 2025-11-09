"""
Given an integer array nums, return true if any value appears more than once in the array, otherwise return false.

This exercise is pretty easy and can be solved in a variety of ways. The most appropriate data structure to be used here 
is a set, because sets do not allow duplicate values. We can iterate through the array and add each element to the set.
If we encounter an element that is already in the set, we can immediately return true.

Or, to make it even shorte in terms of line of code, we can create a set of the array and check whether the length of the set is 
the same as the length of the array. 

The time complexity is O(n), while the space complexity is also O(n).
"""

from typing import List

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        my_set = set(nums)

        return len(my_set) != len(nums)