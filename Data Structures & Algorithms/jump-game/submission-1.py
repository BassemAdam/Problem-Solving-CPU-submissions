class Solution:
    def canJump(self, nums: list[int]) -> bool:
        
        def backtrack(i):
            if i in cache: return cache[i]
            if i >= len(nums) - 1:
                cache[i] = True 
                return True

            steps = nums[i]
            
            if steps == 0: 
                cache[i] = False
                return False
            for j in range(steps,0,-1):
                if i + j >= len(nums) - 1:
                    cache[i] =  True
                    return True  
                if backtrack(j+i):
                    cache[i] =  True
                    return cache[i] 
            cache[i] = False
            return cache[i] 
        cache = {}
        return backtrack(0)
        