## leetcode 1036
## 解数独
## 思路是利用map，并且定义行、列、格子的map list


class Solution:
    ## def isValidSudoku(self, board: List[List[str]]) -> bool:
    def isValidSudoku(self, board):
        # init three maps
        row_map = [ [False for _ in range(10)] for _ in range(9)]
        col_map = [ [False for _ in range(10)] for _ in range(9)]
        box_map = [ [False for _ in range(10)] for _ in range(9)]

        # validate
        for ii in range(9):
            for jj in range(9):
                if board[ii][jj] != '.':
                    num = int(board[ii][jj])
                    box_id = (ii//3) * 3 + jj//3
                    if (row_map[ii][num] or col_map[jj][num] or box_map[box_id][num]):
                        return False
                    else:
                        row_map[ii][num] == True
                        col_map[jj][num] == True
                        box_map[box_id][num] = True
        return True

if __name__ == '__main__':
    s = Solution()
    board = [
            ["8","3",".",".","7",".",".",".","."],
            ["6",".",".","1","9","5",".",".","."],
            [".","9","8",".",".",".",".","6","."],
            ["8",".",".",".","6",".",".",".","3"],
            ["4",".",".","8",".","3",".",".","1"],
            ["7",".",".",".","2",".",".",".","6"],
            [".","6",".",".",".",".","2","8","."],
            [".",".",".","4","1","9",".",".","5"],
            [".",".",".",".","8",".",".","7","9"]
            ]

    print(s.isValidSudoku(board))