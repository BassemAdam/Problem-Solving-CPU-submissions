class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
        R, C = len(board), len(board[0])

        def backtrack(w, i, j):
            # False 
            if not( 0 <= i < R and 0 <= j < C): return False # moved outside
            if board[i][j] == '#': return False # already visited
            if word[w] != board[i][j]: return False # the cell is not the correct letter we need
            
            if w == len(word)-1: return True

            temp = board[i][j]
            board[i][j] = '#'

            found = (
                backtrack(w + 1, i + 1, j) or # move right
                backtrack(w + 1, i, j + 1) or # move up
                backtrack(w + 1, i - 1, j) or # move left
                backtrack(w + 1, i , j - 1)  # move down
            )

 
            board[i][j] = temp
            return found

        for i in range(R):
            for j in range(C):
                if backtrack(0,i,j): return True
        return False