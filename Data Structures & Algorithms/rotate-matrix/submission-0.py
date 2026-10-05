class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        for r in range(n):
            for c in range(r+1,n):
                # Transpose
                matrix[c][r], matrix[r][c]  = matrix[r][c], matrix[c][r] 

        for r in range(n):
                matrix[r].reverse()
                