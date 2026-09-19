class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        r = 0
        currentSum, maxSum = float('-inf'), float('-inf')
        while r < len(nums):
            # reset window we have better start
            if nums[r] > currentSum and currentSum < 0:
                currentSum = 0
            currentSum += nums[r]
            maxSum = max(maxSum,currentSum)
            r +=1
        return maxSum
