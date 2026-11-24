class Solution:
    def isPalindrome(self, s: str) -> bool:
        lower = s.lower()
        new=""
        for c in lower:
            if c.isalnum():
                new+=c
        return new==new[::-1]
