class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # h = {}
        # ptr = 0
        # currLongest = 0
        # longest = 0
        # while ptr < len(s):
        #     c = s[ptr]
        #     if c not in h:
        #         currLongest += 1
        #         h[c] = ptr
        #         ptr += 1
        #         longest = max(longest,currLongest)
        #     else:
        #         currLongest = 0
        #         ptr = h[c]+1
        #         h = {}

        # return longest
        chrSet = set()
        L = 0
        Longest = 0
        for R,c in enumerate(s):
            while c in chrSet:
                chrSet.remove(s[L])
                L +=1
            chrSet.add(c)
            Longest = max(Longest,R - L + 1)

        return Longest
