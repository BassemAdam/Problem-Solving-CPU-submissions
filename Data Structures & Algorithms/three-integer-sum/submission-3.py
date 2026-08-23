class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
       
        d = dict(zip(nums,range(len(nums))))
        ans = []
        for i in range(len(nums)):
            for j in range(len(nums)-1,i,-1):
                compl = -(nums[i] + nums[j])
                k = d.get(compl,-1) 
                inpu = sorted([nums[i],nums[j],nums[k]])
                if k != -1 and inpu not in ans and i != j and j != k and i != k:
                    ans.append(inpu)
        return ans
