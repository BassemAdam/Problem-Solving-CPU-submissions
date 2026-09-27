class Solution:
    def orangesRotting(self, grid: list[list[int]]) -> int:
        R, C = len(grid), len(grid[0])
        queue = deque()

        fresh = 0
        for i in range(R):
            for j in range(C):
                if grid[i][j] == 2:
                    queue.append((i, j))
                if grid[i][j] == 1:
                    fresh += 1

        if fresh == 0:
            return 0

        Time = 0
        while queue and fresh > 0:

            for _ in range(len(queue)):
                r, c = queue.popleft()

                movements = [[1, 0], [-1, 0], [0, 1], [0, -1]]

                for dr, dc in movements:
                    if (
                        0 <= r + dr < R
                        and 0 <= c + dc < C
                        and grid[r + dr][c + dc] == 1
                    ):
                        grid[r + dr][c + dc] = 2
                        queue.append((r + dr, c + dc))
                        fresh -= 1

            Time += 1

        return Time if fresh == 0 else -1
