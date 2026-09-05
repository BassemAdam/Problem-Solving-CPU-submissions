class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        L, R = 0,len(nums) - 1
        if nums[L] < nums[R] or R == 0: return nums[L]

        while L<R:
            mid = (L + R) // 2
            if nums[mid] > nums[R]: # i am in ramp 1 lets search to the right
                L = mid+1
            elif nums[mid] < nums[R]: # i am in ramp 2 lets search to the left
                R = mid


        return nums[L]                            