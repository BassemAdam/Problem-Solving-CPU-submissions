class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 2: return max(nums[0],nums[-1])
        def bottomup(houses):
            if len(houses) <= 2: return max(houses[0],houses[-1])
            dp = [0]* len(houses)
            dp[-1] = houses[-1]
            dp[-2] = max(houses[-2],dp[-1])
        
            for i in range(len(houses)-3,-1,-1):
                dp[i] = max(houses[i] + dp[i+2],dp[i+1])
            
            return dp[0]
        
        return max( bottomup(nums[1:]), bottomup(nums[0:-1]))