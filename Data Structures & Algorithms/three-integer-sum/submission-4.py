class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        d = {num:i for i,num in enumerate(nums)}
        ans = set()
        for i in range(len(nums)):
            if nums[i]> 0: break
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            for j in range(i+1,len(nums)):
                compl = -(nums[i] + nums[j])
                k = d.get(compl,-1) 
                if k != -1 and k > j :
                    inpu = tuple(sorted([nums[i], nums[j], nums[k]]))
                    ans.add(inpu)
        return [t for t in ans]
