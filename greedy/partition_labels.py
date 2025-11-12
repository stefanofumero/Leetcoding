"""
    You are given a string s consisting of lowercase english letters.
    We want to split the string into as many substrings as possible, while ensuring that each letter appears in at most one substring.
    Return a list of integers representing the size of these substrings in the order they appear in the string.


    Here we start iterating over the array. We start from the first
    char and it would be particularly convenient to know where the
    last occurence of that char happens to be. Knowing this helps
    us setting the initial length of the partition to last-first. 

    We are not sure yet that would be enough, so we'll keep two
    vars: size and end, to keep track of where it goes to our
    partition. 

    To keep track of the last index where a char can be found, we use
    an hashMap
"""

from typing import List

class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last_index = {}
        for i,c in enumerate(s):
            last_index[c] = i

        res = []
        size,end = 0,0
        for i,c in enumerate(s):
            size += 1
            end = max(end,last_index[c])

            if i == end:
                res.append(size)
                size = 0
        
        return res

