"""
Given a string s, return true if it is a palindrome, otherwise return false.
A palindrome is a string that reads the same forward and backward. It is also case-insensitive and ignores all 
non-alphanumeric characters. Note: Alphanumeric characters consist of letters (A-Z, a-z) and numbers (0-9).

To solve this problem, we use a double pointer technique: check forward and backward simply
discarding what is not valid as a character
"""

class Solution:
    def isPalindrome(self, s: str) -> bool:
        n = len(s)
        l,r = 0,n-1
        def isValidChar(c:str)->bool:
            #we can accept
            if ord(c) >= ord('a') and ord(c) <= ord('z'):
                return True
            elif ord(c) >= ord('0') and ord(c) <= ord('9'): 
                return True
            else: 
                return False
        
        while l < r:
            c1 = s[l].lower()
            if not isValidChar(c1):
                l += 1
                continue

            c2 = s[r].lower()
            if not isValidChar(c2):
                r -= 1
                continue

            if c1 != c2:
                return False
            l += 1
            r -= 1

        return True            



# There is a much more Pythonic version !!!!
class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1

        while l < r:
            while l < r and not s[l].isalnum():
                l += 1
            while l < r and not s[r].isalnum():
                r -= 1
            
            if s[l].lower() != s[r].lower():
                return False
            
            l += 1
            r -= 1
        
        return True