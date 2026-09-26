class Solution:
    def insert(self, intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]:
        if not intervals: return [newInterval]
        overlapp = []
        def isOverlap(newInterval,interval):
            if interval[0] <= newInterval[0] <= interval[1]:
                return True
            elif newInterval[0] <= interval[0] <= newInterval[1] :
                return True
            elif newInterval[0] <= interval[1] <= newInterval[1] :
                return True
            return False
        
        for i in range(len(intervals)):
            if isOverlap(newInterval,intervals[i]):
                overlapp.append(True)
            else:
                overlapp.append(False)

        ans = []
        s = None
        e = None
        for i in range(len(intervals)):
            if overlapp[i]:
                if s == None:
                    s = min(newInterval[0], intervals[i][0])
                e = max(newInterval[1],intervals[i][1])
            else:
                ans.append(intervals[i])

        if s == None:
            ans.append(newInterval)
        else:
            ans.append([s,e])
            
        ans.sort(key = lambda x : x[0])
        return ans