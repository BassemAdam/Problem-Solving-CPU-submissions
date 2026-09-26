class Solution:
    def maxAreaOfIsland(self, grid: list[list[int]]) -> int:
        R,C = len(grid),len(grid[0])

        self.maxArea = float('-inf')
        def dfs(r,c):
            if min(r,c) < 0:
                return 0
            if r == R or c == C:
                return 0
            if grid[r][c] == 0:
                return 0
            self.currentArea += 1
            self.maxArea = max(self.maxArea,self.currentArea)

            grid[r][c] = 0

            dfs(r+1,c)
            dfs(r-1,c)
            dfs(r,c+1)
            dfs(r,c-1)
        

        for r in range(R):
            for c in range(C):
                if grid[r][c] == 1:
                    self.currentArea = 0
                    dfs(r,c)
        return self.maxArea if self.maxArea != float('-inf') else 0