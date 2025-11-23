"""
Given an array of integers nums, return the length of the longest consecutive sequence of elements that can be formed.
A consecutive sequence is a sequence of elements in which each element is exactly 1 greater than the previous element. The elements do not have to be consecutive in the original array.
You must write an algorithm that runs in O(n) time.


There's let's say a straight forward way to solve this problem: order the array and check with a linear cycle over the sorted array the length
of the longest sequence. This is O(nlog(n)) time and O(1) or O(n) space depending on the sorting algorithm.

Another option would be to use a set. We can check,for each element, whether there's the element-1 in the set, as in this case that would be the beginning
of a sequence. In case it is not presente, we cycle while number + i is present, incrementing the counter
"""

from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        longest = 0
        numSet = set(nums)

        for num in nums:
            if (num-1) not in numSet:
                cnt = 1
                while num + cnt in numSet:
                    cnt += 1
                longest = max(longest,cnt)
         

        return longest
        
