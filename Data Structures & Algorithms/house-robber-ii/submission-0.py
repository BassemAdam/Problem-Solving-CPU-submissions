class Solution:
    def rob(self, nums: List[int]) -> int:
        
        def dfs(i,zeroIncluded):
            if i >= len(nums):
                return 0
            if zeroIncluded and i == len(nums) -1:
                return 0
            
            state = (i,zeroIncluded)
            if state in cache: return cache[state]

            flag = zeroIncluded or (i == 0)
            rob = nums[i] + dfs(i+2,flag)
            skip = dfs(i+1,zeroIncluded)
            cache[state] = max(rob,skip)
            return cache[state]
        cache = {}
        return dfs(0,False)