"""
Given an integer array nums, return an array output where output[i] is the product of all the elements of nums except nums[i].

Each product is guaranteed to fit in a 32-bit integer.

Follow-up: Could you solve it in O(n) O(n) time without using the division operation?


To solve this exercise, we start with a simple version where we use division.

In particular, we first count the number of values set to zero, if it is more than one, then the output is an array full
of zeros. If it's only one zero, all elements except that are zeros. If there are no zeros, the value of each element
is the total product divided by that value.

The second version, which is more complex, is based on a prefix/suffix strategy. The idea behind it is pretty simple:
for each element, the result is the multiplication of all the elements on its left by all the elements on its right.
We can reproduce this behaviour using a prefix and a suffix. We first multiply each element by the predecessors,
so that each i in the output is the value of the multiplication of the left elements, then we do the same on the
opposite side, so that it contains the correct output at the end.

Overall, time complexity is O(n), while space complexity is O(n).
"""

from typing import List
class Solution:
    def productExceptSelf(self,nums:List[int])->List[int]:
        number_of_zeros = sum(num == 0 for num in nums)
        if number_of_zeros > 1:
            return [0] * len(nums)
        
        tot_product = 1
        for n in nums:
            if n != 0:
                tot_product *= n 

        sol = [1] * len(nums)

        for i in range(len(nums)):
            if number_of_zeros == 0:
                sol[i] = int(tot_product/nums[i])
            elif number_of_zeros and nums[i] != 0:
                sol[i] = 0
            else:
                sol[i] = int(tot_product)

        return sol
    
    def productExceptSelf_prefSuffix(self,nums:List[int])->List[int]:
        pref,suff = 1,1
        res = [1] * len(nums)
        #first, prefix multiplication
        for i in range(len(nums)):
            res[i] = pref
            pref *= nums[i]
        
        for i in range(len(nums)-1,-1,-1):
            res[i] *= suff
            suff *= nums[i]

        return nums