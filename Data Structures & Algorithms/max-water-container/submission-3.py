class Solution:
    def maxArea(self, height: List[int]) -> int:
        # ptrL = 0
        # ptrR = len(height) - 1
        # maxA = min(height[ptrL],height[ptrR])*(ptrR - ptrL)
        # for i in range(len(height)):
        #     for j in range(i+1,len(height)):
        #         A = min(height[i],height[j])*(j - i)
        #         maxA = max(maxA,A)
        # return maxA
        ptrL = 0
        ptrR = len(height) - 1
        maxA = -1
        while ptrL < ptrR:
                A = min(height[ptrL],height[ptrR])*(ptrR - ptrL)
                maxA = max(maxA,A)
                if height[ptrL] < height[ptrR]:
                    ptrL +=1
                else:
                    ptrR -=1
        return maxA