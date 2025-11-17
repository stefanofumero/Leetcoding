"""
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]]
 where nums[i] + nums[j] + nums[k] == 0, and the indices i, j and k are all distinct.
The output should not contain any duplicate triplets. You may return the output and the triplets in any order.

To reduce the time complexity of this exercise (which would be O(n^3) brute forcing), we can order the array:
For each value, we search in the remaining part of the array through a double pointer strategy to find whether
there's a couple that sums to target.

The most complex part is definitely here:
                    while nums[l] == nums[l-1] and l<r:
                        l += 1

when it finds a correspondance, it has to move l making sure there are no duplicates. Remember you've already moved l
there, so you check whether it is the same as the previous one, in case skip and go on. You don't need to do the same 
for r, because, as l changes, for sure there won't be a duplicate if r doesn't change.
"""
from typing import List

class Solution:

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums) 
        i = 0

        nums.sort() #sorted in ascending order

        while i <= n-2:
            if nums[i] > 0:
                break

            if i and nums[i] == nums[i-1]:
                i += 1
                continue

            l,r = i+1, n - 1
            while l < r:
                val = nums[i] + nums[l] + nums[r]
                if val == 0:
                    res.append([i,l,r])
                    l += 1
                    r -= 1
                    #Only in case of a correspondance, avoid duplicates...
                    while nums[l] == nums[l-1] and l<r:
                        l += 1
                elif val < 0:
                    l += 1
                else:
                    r -= 1

            i += 1
                
        return res