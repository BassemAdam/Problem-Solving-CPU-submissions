class Solution:
    def pacificAtlantic(self, heights: list[list[int]]) -> list[list[int]]:
        
        R,C = len(heights),len(heights[0])

        def dfs(r,c,pr,pc,visited):
            nonlocal canFlowToNW , canFlowToSE
            if (min(r,c) < 0):
                canFlowToNW = True
                return 
            # can flow to Atlantic
            if r == R or c == C:
                canFlowToSE = True
                return 
            # the rain will not come from a lower height ground than me
            if heights[r][c] > heights[pr][pc] or ((r,c) in visited):
                return 
            # can flow to Pacific

            visited.add((r,c))
            dfs(r-1,c,r,c,visited)  
            dfs(r,c-1,r,c,visited) 
            dfs(r+1,c,r,c,visited)  
            dfs(r,c+1,r,c,visited)


        ans = []
        canFlowToNW, canFlowToSE = False, False
        visited = set()
        for r in range(R):
            for c in range(C):
                dfs(r,c,r,c,visited)
                if canFlowToNW and canFlowToSE:
                    ans.append((r,c))
                canFlowToNW, canFlowToSE = False, False
                visited = set()
        return ans

        