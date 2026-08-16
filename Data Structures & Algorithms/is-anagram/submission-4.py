class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False

        # solution 1
        # s = list(s)
        # t = list(t)
        # s.sort()
        # t.sort()
        # for i in range(len(s)):
        #     if s[i] != t[i]:
        #         return False
        # return True

        # solution 2
        # return sorted(s) == sorted(t)

        # solution 3
        d = {}
        for i in range(len(s)):
            d[s[i]] = d[s[i]] + 1 if s[i] in d else 1
            d[t[i]] = d[t[i]] - 1 if t[i] in d else -1
        
        return all(count == 0 for count in d.values())
        