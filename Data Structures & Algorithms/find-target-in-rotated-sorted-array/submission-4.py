class Solution:
    def search(self, nums: List[int], target: int) -> int:
        L, R = 0,len(nums) - 1
        if len(nums) == 1 and nums[0] == target: return 0


        while L<R:
            mid = (L + R) // 2
            if nums[mid] > nums[R]: # i am in ramp 1 lets search to the right
                L = mid+1
            elif nums[mid] < nums[R]: # i am in ramp 2 lets search to the left
                R = mid
        
        print(L)
        L1,R1 = L,len(nums)-1
        while L1<R1:
            mid = (L1 + R1) // 2
            if nums[mid] < target: 
                L1 = mid+1
            elif nums[mid] > target: 
                R1 = mid
            else:
                return mid

        if nums[L1] == target:
            return L1

        L2,R2 = 0,R
        while L2<R2:
            mid = (L2 + R2) // 2
            if nums[mid] < target: 
                L2 = mid+1
            elif nums[mid] > target: 
                R2 = mid
            else:
                return mid
        
        if nums[L2] == target:
            return L2

        return -1
                  