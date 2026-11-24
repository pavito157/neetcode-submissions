class Solution:
    def isPalindrome(self, s: str) -> bool:
        lower = s.lower()
        new=""
        for c in lower:
            if c.isalnum():
                new+=c
        if new[::-1]==new:
            return True
        return False
