class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Solution 1 : Brute Force
        # out=[1] * len(nums)
        # for i in range(len(nums)):
        #     for j in range(len(nums)):
        #         if i == j: continue
        #         out[i] *=nums[j]
        # return out

        # Solution 2 : 
        res = 1
        numOfZeros = 0
        for i in range(len(nums)):
            res *=nums[i]
            if nums[i] == 0:
                numOfZeros+=1
        if numOfZeros >=2: return [0] * len(nums)
        out = [res]* len(nums)
        
        for j in range(len(nums)):
            if nums[j] == 0:
                res = 1
                for i in range(len(nums)):
                    if nums[i] == 0: continue
                    res *=nums[i]
                out[j] = res
            else:
                out[j] = out[j] // nums[j]
        return out