class Solution:
    def minWindow(self, s: str, target: str) -> str:
        ans = ""
        l = 0
        
        t = {}
        for c in target:
                t[c] = t.get(c, 0) + 1

        windowFreq = {} 
        minLength = float('inf')

        def isValid():
            for chr,count in t.items():
                if windowFreq.get(chr,0) < count:
                    return False
            return True
        bestl = -1
        bestr = -1
        for r in range(len(s)):
            chr = s[r]
            if chr in t:
                windowFreq[chr] = windowFreq.get(chr,0) + 1  
                
            while isValid():
                if minLength > r - l + 1:
                    minLength = r - l + 1
                    bestl = l
                    bestr = r
                    #ans = s[l:r+1]

                if s[l] in windowFreq: windowFreq[s[l]] -= 1
                l +=1
                

        return "" if minLength == float('inf') else s[bestl:bestr+1]
