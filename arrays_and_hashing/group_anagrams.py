"""
Given an array of strings strs, group all anagrams together into sublists. You may return the output in any order.
An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.


This exercise, despite being medium, is pretty complex. It requires some knowledge of Python details to be solved. The idea
behind is similar to the one in valid_anagram: two strings are anagrams of each other if they have the sane characters.

Thus, the trick is to consider the counter representing the number of characters in a string as the key of a dictionary.
All strings with the same key are placed in a list that is the value of the aforementioned dictionary. Where's the Pyhton knowledge needed?

A dictionary (hashMap) key is valid in Python only if it is hashable and, in order to be hashable, it has to be unique: we cannot use
a list because it is a mutable object in Python. There are many solution to this problem, the first one coming to my mind is to use
a string, which is indeed immutable. The simplest one is to use a tuple, and that's what I'll do here.
"""
from typing import List
from collections import defaultdict

class Solution:
    def groupAnagrams(self,strs:List[str])->List[List[str]]:
        sol = defaultdict(list) #a dict of empty lists by default

        for word in strs:
            char_counter = [0]*26
            for c in word:
                char_normalized = c.lower()
                char_counter[ord(char_normalized)-ord('a')] += 1

            sol[tuple(char_counter)].append(word)

        return [sublist for sublist in sol.values()]