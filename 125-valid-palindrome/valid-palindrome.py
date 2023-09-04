import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        l=s.lower()
        S=re.sub(r"[^a-z0-9]","",l)
        if S=="" or (S==S[::-1]):
            return True
        else:
            return False

        