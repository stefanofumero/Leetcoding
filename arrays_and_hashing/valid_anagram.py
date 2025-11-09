"""
Given two strings s and t, return true if the two strings are anagrams of each other, otherwise return false.
An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.

The second statement of the exercise is particularly useful to understand how to solve this problem. Indeed, we can use an hashmap to 
count the characters of each string. This is still O(1) in terms of memory because we have 26 possible chars in a string (lowercase). 
The time complexity is O(n), where n is the length of s, which is the same as the length of t, otherwise they could not be anagrams
of each other. In a more readable version, I could have used a single counter where I added the occurrences of one string and 
subtracted the occurrences of the other, then I should have checked if all elements are zeros.

If the two are the same, then one string is the anagram of the other.


"""

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
            counter_s = [0]*26
            counter_t = [0]*26

            if len(s) != len(t):
                return False
            
            for i in range(len(s)):
                char_s = s[i].lower()
                char_t = t[i].lower()
                counter_s[ord(char_s)-ord('a')] += 1
                counter_t[ord(char_t)-ord('a')] += 1

            return all(counter_s[i] == counter_t[i] for i in range(len(counter_t)))

