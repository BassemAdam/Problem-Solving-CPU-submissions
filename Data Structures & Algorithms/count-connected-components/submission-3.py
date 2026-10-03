class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        adjList = {i: [] for i in range(n)}
        for src, dst in edges:
            adjList[src].append(dst)
            adjList[dst].append(src)
        
        visited = set()
        numOfComponent = 0

        def dfs(node):
            visited.add(node)
            for nei in adjList[node]:
                if nei not in visited:
                    dfs(nei)

            return

        for i in range(n):
            if i not in visited:
                dfs(i)
                numOfComponent += 1
            if len(visited) == n:
                return numOfComponent