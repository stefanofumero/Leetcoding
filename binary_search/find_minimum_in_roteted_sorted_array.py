"""
You are given an array of length n which was originally sorted in ascending order. It has now been rotated between 1 and n times. For example, the array nums = [1,2,3,4,5,6] might become:
[3,4,5,6,1,2] if it was rotated 4 times.
[1,2,3,4,5,6] if it was rotated 6 times.
Notice that rotating the array 4 times moves the last four elements of the array to the beginning. Rotating the array 6 times produces the original array.
Assuming all elements in the rotated sorted array nums are unique, return the minimum element of this array.
A solution that runs in O(n) time is trivial, can you write an algorithm that runs in O(log n) time?

This exercise is very complex (in my honest opinion). There are many edge cases to consider.
First thing: since it requires O(log n) time, we have to use binary search.
We start with an array that goes from l to r (pointers that stands for left and right extremes of the array).
Initially, we set the result to nums[0] (this is arbitrary).
At each step, we check whether we are in a subportion of the array that is sorted. In that case, we update result (if it is necessary) and
break the loop. This is because the pivot cannot be in the middle of a sorted array. Otherwise, we check in the unsorted half of the array when 
breaking it in two halves.

Pay attention to > or >= when comparing nums[m] and nums[l]. Consider the edge case when there are just two elements in the array and it is 
sorted in decreasing order (e.g. [2,1]). In that case, if we use >, we return 2.
"""
from typing import List

class Solution:
    def findMin(self, nums: List[int]) -> int:
        res = nums[0]
        l,r = 0,len(nums)-1

        while l <= r:
            if nums[l] <= nums[r]:
                res = min(res,nums[l])
                break

            m = (l+r)//2
            res = min(res, nums[m])
            if nums[m] >= nums[l]: 
                l = m + 1
            else:
                r = m - 1 

        return res