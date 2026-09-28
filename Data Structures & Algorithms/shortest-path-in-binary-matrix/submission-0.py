class Solution:
    def shortestPathBinaryMatrix(self, grid: list[list[int]]) -> int:
        R, C = len(grid),len(grid)
        queue = deque()
        queue.append((0, 0))
        visited = set()

        Reached = False
        globalShortest = float('inf')
        ShortestPath = 1
        while queue:

            for _ in range(len(queue)):

                r, c = queue.popleft()
                movements = [[1, 0], [-1, 0], [0, 1], [0, -1], [1, 1], [-1, -1],[-1,1],[1,-1]]
                for dr, dc in movements:
                    nr, nc = r + dr, c + dc
                    if  grid[r][c] == 1: break
                    if nr == R and nc == C:
                        Reached = True
                        break
                    if (
                        not (0 <= nr < R and 0 <= nc < C)
                        or (nr, nc) in visited
                        or grid[nr][nc] == 1
                    ):
                        continue

                    visited.add((nr, nc))
                    queue.append((nr,nc))

            if Reached: break
            ShortestPath += 1

        return ShortestPath if Reached else -1
