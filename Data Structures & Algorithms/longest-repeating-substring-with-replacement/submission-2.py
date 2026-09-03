class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = {}
        L = 0
        longest = -1
        for R in range(len(s)):
            chr = s[R]
            freq[chr] = freq.get(chr,0) + 1
            valid = R - L + 1 - max(freq.values(),default = 0)<=k
            if valid:
                longest = max(longest,R-L+1)
            else:
                freq[s[L]] = freq.get(s[L],0) - 1
                L += 1
        return longest


    
        