class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False

        # solution 1
        # s = list(s) # Space O(n)
        # t = list(t) # Space O(n)
        # s.sort() # Time O(nlongn)
        # t.sort() # Time O(nlongn)
        # for i in range(len(s)): # Time O(n)
        #     if s[i] != t[i]: # Time O(1)
        #         return False
        # return True

        # Complexity : Time O(nlogn) Space O(n) 
        #-----------------------------------------------
        
        # solution 2
        # return sorted(s) == sorted(t) 
        
        # Complexity : Time O(2nlogn) Space O(2n) not in place
        #-----------------------------------------------

        # solution 3
        d = {} # Space O(n)
        for i in range(len(s)): # Time O(n)
            d[s[i]] = d.get(s[i], 0) + 1 # Time O(1)
            d[t[i]] = d.get(t[i], 0) - 1 # Time O(1)
        
        return all(count == 0 for count in d.values()) # Time O(k) where k is unique lowercase english letters
        # Complexity : Time O(n) Space O(n)
        #-----------------------------------------------
        
        # Practical Usability 
        # 1- Checking Differences and syncing state 