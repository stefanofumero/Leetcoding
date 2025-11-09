"""
Given an array of integers nums and an integer target, return the indices i and j such that nums[i] + nums[j] == target and i != j.
You may assume that every input has exactly one pair of indices i and j that satisfy the condition.
Return the answer with the smaller index first.


To solve this exercise, I can use a pretty famous strategy that is based on a trick:
in order to have nums[i] + nums[j] == target then, for a whatever number in the array nums[i], I need a nums[j] = target - nums[i]

Thus, for each number I scan in the array, I can store in an hashmap what it was missing to reach the target and the corresponding index as
a value. For each new number I encounter in the array, let's check if there's a correspondance in the hashmap, otherwise store it 
and go on.

This solution is O(n) in terms of time complexity, while it is O(1) in terms of memory complexity
"""
from typing import List


class Solution:
    def twoSum(self,nums:List[int],target:int)->List[int]:
        occurrencies_map = {}

        for i,n in enumerate(nums):
            if n in occurrencies_map:
                return [occurrencies_map[n],i]
            else:
                occurrencies_map[target-n] = i
            