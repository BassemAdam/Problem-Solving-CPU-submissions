class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        R,C = len(matrix), len(matrix[0])

        rowsToRemove = []
        colsToRemove = []
        for i in range(R):
            for j in range(C):
                if matrix[i][j] == 0:
                    rowsToRemove.append(i)
                    colsToRemove.append(j)
        for r in rowsToRemove:
            for i in range(C):
                matrix[r][i] = 0
        for c in colsToRemove:
            for i in range(R):
                matrix[i][c] = 0
                    