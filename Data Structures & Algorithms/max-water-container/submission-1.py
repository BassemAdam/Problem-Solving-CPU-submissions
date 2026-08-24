class Solution:
    def maxArea(self, height: List[int]) -> int:
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