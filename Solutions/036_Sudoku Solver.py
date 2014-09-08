# @TODO
# Time Limit Exceeded
# [".....7..9",".4..812..","...9...1.","..53...72","293....5.",".....53..","8...23...","7...5..4.","531.7...."]


class Solution:
    # @param board, a 9x9 2D array
    # Solve the Sudoku by modifying the input board in-place.
    # Do not return any value.

    def solveSudoku(self, board):
        def isValid(x, y):
            tmp = board[x][y]
            board[x][y] = 'D'
            for i in range(9):
                if board[i][y] == tmp:
                    return False
            for i in range(9):
                if board[x][i] == tmp:
                    return False
            for i in range(3):
                for j in range(3):
                    if board[(x / 3) * 3 + i][(y / 3) * 3 + j] == tmp:
                        return False
            board[x][y] = tmp
            return True

        def dfs(board):
            for i in range(9):
                for j in range(9):
                    if board[i][j] == '.':
                        for k in '123456789':
                            board[i][j] = k
                            if isValid(i, j) and dfs(board):
                                return True
                            board[i][j] = '.'
                        return False
            return True
        dfs(board)
