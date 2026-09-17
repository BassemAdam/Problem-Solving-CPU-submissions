class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        
        self.combinations = []
    
        def bf(arr,target,start,currComb):
            if sum(currComb) > target: return 
                  
            for i in range(start,len(arr)):
                #choose
                currComb.append(arr[i])
                if sum(currComb) == target:
                    self.combinations.append(currComb.copy())
                    currComb.pop()    
                    continue
                # explore recurse
                bf(arr,target,i,currComb)
                # unchoose
                currComb.pop()         

        bf(candidates,target,0,[])
        return self.combinations