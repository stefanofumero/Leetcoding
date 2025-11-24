"""
You are given an array of length n which was originally sorted in ascending order. It has now been rotated between 1 and n times. For example, the array nums = [1,2,3,4,5,6] might become:
[3,4,5,6,1,2] if it was rotated 4 times.
[1,2,3,4,5,6] if it was rotated 6 times.
Given the rotated sorted array nums and an integer target, return the index of target within nums, or -1 if it is not present.
You may assume all elements in the sorted rotated array nums are unique,
A solution that runs in O(n) time is trivial, can you write an algorithm that runs in O(log n) time?


Here the trick is to have understood 'find_minimum_in_a_rotated_sorted_array.py' and then look at possible examples to really get the logic.
When you look at a middle point, if the left side is lower equal then the middle, then you are in the sorted side. If the target is in that
range, then you can discard the right side. If it's not, go right. When the left side is not sorted, it means the right one it is. 
Once you know the right side is sorted, you can check if the target is in that range to discard the left side or not.

This is pretty simple, look at examples (I'm joking, it is simple once you understood it)
"""


from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l,r = 0, len(nums)-1

        while l <= r:
            m = (l+r)//2
            if target == nums[m]:
                return m

            if nums[l] <= nums[m]: #the left side is sorted
                if target >= nums[l] and target <= nums[m]:
                    r = m-1
                else:
                    l = m+1
            else: # the right side is sorted
                if target > nums[r] or target < nums[m]:
                    r = m-1
                else:
                    l = m+1
        
        return -1
            