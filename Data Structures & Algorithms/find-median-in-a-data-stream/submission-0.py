class MedianFinder:

    def __init__(self):
        self.Lmaxheap,self.Rminheap = [], []

    def addNum(self, num: int) -> None:
        if not self.Lmaxheap or num <= self.Lmaxheap[0]:
            heapq.heappush_max(self.Lmaxheap,num)
        else:
            heapq.heappush(self.Rminheap,num)

        if  len(self.Lmaxheap) - len(self.Rminheap) > 1:
            popNum = heapq.heappop_max(self.Lmaxheap)
            heapq.heappush(self.Rminheap,popNum)
        if  len(self.Rminheap) - len(self.Lmaxheap) > 1:
            popNum = heapq.heappop(self.Rminheap)
            heapq.heappush_max(self.Lmaxheap,popNum)


    def findMedian(self) -> float:
        if len(self.Lmaxheap) == len(self.Rminheap):
            return (self.Lmaxheap[0] + self.Rminheap[0]) / 2
        elif len(self.Lmaxheap) > len(self.Rminheap):
            return self.Lmaxheap[0]
        else:
            return self.Rminheap[0]