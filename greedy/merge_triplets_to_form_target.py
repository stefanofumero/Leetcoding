"""
    You are given a 2D array of integers triplets, where triplets[i] = [ai, bi, ci] represents the ith triplet. You are also given an array of integers target = [x, y, z] which is the triplet we want to obtain.
    To obtain target, you may apply the following operation on triplets zero or more times:
    Choose two different triplets triplets[i] and triplets[j] and update triplets[j] to become [max(ai, aj), max(bi, bj), max(ci, cj)].
    * E.g. if triplets[i] = [1, 3, 1] and triplets[j] = [2, 1, 2], triplets[j] will be updated to [max(1, 2), max(3, 1), max(1, 2)] = [2, 3, 2].
    Return true if it is possible to obtain target as an element of triplets, or false otherwise.

    To be feasible to reach the target, we need that there 
    exist a triplet containing, in position i, the value 
    that the target wants in position i. But also, the other 
    elements in the triplets should not be higher than the 
    target, otherwise it is not possible to 'revert'.

    What we can do is:keep 3 flags, one for each pos in the 
    target array. If you find a triplet satisfying the prev 
    condition on one of the three pos, then check a flag.
    Once all the three flags are checked, you can go on and
    return true, otherwise false
"""

from typing import List

class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        flg0,flg1,flg2 = False,False,False

        for triplet in triplets:
            #check 0
            if triplet[0] == target[0] and triplet[1] <= target[1] and triplet[2] <= target[2]:
                flg0 = True
            #check 1
            if triplet[1] == target[1] and triplet[0] <= target[0] and triplet[2] <= target[2]:
                flg1 = True
            #check2
            if triplet[2] == target[2] and triplet[1] <= target[1] and triplet[0] <= target[0]:
                flg2 = True

            if flg0 and flg1 and flg2:
                return True

        return False
