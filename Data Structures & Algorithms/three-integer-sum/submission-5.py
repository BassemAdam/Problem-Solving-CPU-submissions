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
        # nums.sort()
        # d = {num:i for i,num in enumerate(nums)}
        # ans = set()
        # for i in range(len(nums)):
        #     if nums[i]> 0: break
        #     if i > 0 and nums[i] == nums[i - 1]:
        #         continue
        #     for j in range(i+1,len(nums)):
        #         compl = -(nums[i] + nums[j])
        #         k = d.get(compl,-1) 
        #         if k != -1 and k > j :
        #             inpu = tuple(sorted([nums[i], nums[j], nums[k]]))
        #             ans.add(inpu)
        # return [t for t in ans]
