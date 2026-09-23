class Solution:
    def rob(self, houses: List[int]) -> int:

        if len(houses) <= 2: return max(houses[0],houses[-1])
        dp = [0]* len(houses)
        dp[-1] = houses[-1]
        dp[-2] = max(houses[-2],dp[-1])
    
        for i in range(len(houses)-3,-1,-1):
            dp[i] = max(houses[i] + dp[i+2],dp[i+1])
        
        return dp[0]