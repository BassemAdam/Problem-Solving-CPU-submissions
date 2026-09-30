class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        adjList = {}
        for dst,src in prerequisites:
            if src not in adjList:
                adjList[src] = []
            if dst not in adjList: 
                adjList[dst] = []
            adjList[src].append(dst)
        

        visited = set()
        currentlyVisiting = set()

        def dfs(node):
            if node in visited: return True
            if node in currentlyVisiting: return False

            currentlyVisiting.add(node)

            for nei in adjList[node]:
                if not dfs(nei):
                    return False

            currentlyVisiting.remove(node)
            visited.add(node)   
            return True

        for desiredCourse,prerequisiteCourse in prerequisites:
                if not dfs(prerequisiteCourse):
                    return False


        return True