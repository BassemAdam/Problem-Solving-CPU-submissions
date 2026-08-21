class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        d = {}
        nums.sort()
        for num in nums:
            d[num] = 0

        for num in nums:
            if num-1 in d:
                d[num] = 1 + d[num-1]
            else:
                d[num] = 1
        print(d.values())
        if d.values():
            return max(d.values())
        else:
            return 0