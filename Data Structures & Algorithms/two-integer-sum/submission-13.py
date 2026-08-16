class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        # solution 1
        d = {}
        for i in range(len(nums)):
            d[nums[i]] = i
        for i in range(len(nums)):
            ptrJValue = target - nums[i]
            if ptrJValue in d and i != d[ptrJValue]:
                return [i,d[ptrJValue]] 
        