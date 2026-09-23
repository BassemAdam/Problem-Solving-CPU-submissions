class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        R, C = len(grid), len(grid[0])

        def dfs(r, c):
            if min(r, c) < 0:
                return 
            if r == R or c == C:
                return 
            if grid[r][c] == "0":
                return 

            grid[r][c] = "0"

            dfs(r + 1, c)
            dfs(r - 1, c) 
            dfs(r, c + 1) 
            dfs(r, c - 1)

        numberOfIslands = 0
        for i in range(R):
            for j in range(C):
                if grid[i][j] == "1":
                    numberOfIslands += 1
                    dfs(i, j)

        return numberOfIslands
