class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = "".join( c.lower() for c in s if c.isalnum())
        if len(s) == 0: return True
        rPtr = 0
        lPtr = len(s)-1
        while(s[rPtr] == s[lPtr]):
            rPtr += 1
            lPtr -= 1
            if rPtr > lPtr:
                return True
        return False 
            