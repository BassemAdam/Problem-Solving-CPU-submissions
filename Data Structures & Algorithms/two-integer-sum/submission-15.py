class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        # solution 1 - Hashmap
        # d = {} # Space O(n)
        # for i in range(len(nums)): # Time O(n)
        #     d[nums[i]] = i # Time O(1) worst case O(n) propagation
        # for i in range(len(nums)): # Time O(n)
        #     ptrJValue = target - nums[i] # Time O(1)
        #     if ptrJValue in d and i != d[ptrJValue]: # Time O(1)
        #         return [i,d[ptrJValue]] # Time O(1)
        # Complexity : Time O(n) Space O(n)
        #----------------------------------------------------------------

        # solution 2 - Brute Force
        # for i in range(len(nums)):
        #     for j in range(len(nums)):
        #         if nums[i] + nums[j] == target and i != j:
        #             return [i,j]
        # Complexity : Time O(n^2) Space O(2)
        #----------------------------------------------------------------
        
        # solution 1 - better rewritten 
        d = {}
        for i,num in enumerate(nums):
            complement = target - num
            if complement in d:
                return sorted([i,d[complement]])
            d[num] = i
        # Practical Usability
        # 