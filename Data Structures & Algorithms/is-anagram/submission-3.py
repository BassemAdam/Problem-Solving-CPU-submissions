class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        # solution 1
        # if len(s) != len(t): return False
        # s = list(s)
        # t = list(t)
        # s.sort()
        # t.sort()
        # for i in range(len(s)):
        #     if s[i] != t[i]:
        #         return False
        # return True

        # solution 2
        return sorted(s) == sorted(t)