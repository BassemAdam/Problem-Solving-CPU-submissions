class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        adjList = {i: [] for i in range(n)}
        for src, dst in edges:
            adjList[src].append(dst)
            adjList[dst].append(src)
        

        def dfs(node):
            nonlocal numOfComponent 
            if node in visited:
                return
            
            visited.add(node)
            for nei in adjList[node]:
                dfs(nei)

            return


        visited = set()
        numOfComponent = 0
        for i in range(n):
            if i not in visited:
                dfs(i)
                numOfComponent += 1
            if len(visited) == n:
                return numOfComponent