class Solution:
    # @return an integer

    def totalNQueens(self, n):
        def check(k, j):  # check if the kth queen can be put in column j!
            for i in range(k):
                if board[i] == j or abs(k - i) == abs(board[i] - j):
                    return False
            return True
        board = [-1 for i in range(n)]
        row = 0
        col = 0
        sum = 0
        while row < n:
            while col < n:
                if check(row, col):
                    board[row] = col
                    col = 0
                    break
                else:
                    col += 1
            if board[row] == -1:
                 # 如果为真，即为在这一行找不到位置放置皇后
                if row == 0:
                    # 如果在第0行也找不到位置放置皇后了，说明所有的情况已经迭代完毕了，执行break跳出操作。
                    break
                else:
                    row -= 1  # 这条语句用来回溯到上一行
                    col = board[row] + 1  # 回溯到上一行时，皇后放置的位置要加1，也就是开始试验下一列
                    board[row] = -1  # 然后将这一行的值重置为-1，也就是说要重新寻找皇后的位置了
                    continue
            if row == n - 1:
                # 当row==n-1时，说明最后一行的皇后位置也确定了，得到了一个解
                sum += 1
                col = board[row] + 1
                board[row] = -1
                continue
            row += 1
        return sum
