class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = "".join( c.lower() for c in s if c.isalnum())
        if len(s) == 0: return True
        rPtr = 0
        lPtr = len(s)-1
        print(f"s[rPtr] :{s[rPtr]} & s[lPtr] : {s[lPtr]}")
        while(s[rPtr].lower() == s[lPtr].lower()):
            rPtr += 1
            lPtr -= 1
            if rPtr > lPtr:
                return True
        return False 
            