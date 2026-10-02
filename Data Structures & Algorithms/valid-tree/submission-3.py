class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if n == 1: return True
        adjList = {}
        for src, dst in edges:
            if src not in adjList:
                adjList[src] = []
            if dst not in adjList:
                adjList[dst] = []
            adjList[src].append(dst)
            adjList[dst].append(src)
        
        

        def dfs(src,preSrc):
            if src in visiting:
                return False
            if src in visited:
                return True
            visiting.add(src)
            for dst in adjList[src]:
                if dst == preSrc:
                    continue
                print(f"src: {src} dst: {dst}")
                if not dfs(dst,src):
                    return False
            visiting.remove(src)
            visited.add(src)
            return True
            
        visited = set()
        visiting = set()

     
        if not dfs(0,0):
            return False
        for src, _ in adjList.items():
            if src not in visited:
                return False
        return True