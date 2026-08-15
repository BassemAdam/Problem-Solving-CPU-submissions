class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # solution 1
        # d = {}
        # for num in nums:
        #     d[num] = d[num] + 1 if num in d else 1 
        #     if d[num] == 2:
        #         return True
        # return False 
        #-------------------------------------
        # solution 2
        nums.sort()
        for i in range(len(nums) - 1):
            if nums[i] == nums[i+1]:
                return True
        return False