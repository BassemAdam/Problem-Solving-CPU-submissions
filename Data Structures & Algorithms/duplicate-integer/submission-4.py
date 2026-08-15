class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        # Practical Usability : identify duplication in Api payload business logic or idempotency in specific list
        #--------------------------------------

        # solution 1
        # Time O(n) avg 
        # note # 1 that dictionery lookup can degrade in the worst case to become O(n) 
        # instead of O(1) so in worst case Time could be O(n^2) rarely
        # Space O(n)
        # d = {}
        # for num in nums:
        #     d[num] = d[num] + 1 if num in d else 1 
        #     if d[num] == 2:
        #         return True
        # return False 

        #-------------------------------------

        # solution 2
        # Time O(nlogn + n = nlogn) python Timsort  
        # space O(0)
        # nums.sort()
        # for i in range(len(nums) - 1):
        #     if nums[i] == nums[i+1]:
        #         return True
        # return False

        # solution 3
        return len(nums) != len(set(nums))