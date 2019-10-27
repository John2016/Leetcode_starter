## leetcode 37
## 解数独
## 基于第36题，加入回溯

class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        def is_available(row, col, box, num):
            box_index = (row // 3) * 3 + col//3
            return not (rol_map[row][num] or col_map[col][num] or box_map[box_index][num])

        def insert_num(row, col, box, num):
            rol_map[row][num] = True
            col_map[col][num] = True
            box_map[box][num] = True
            board[row][col] = str(num)


        def remove_num():
            rol_map[row][num] = False
            col_map[col][num] = False
            box_map[box][num] = False
            board[row][col] = '.'
        
        def add_next(row, col):
            if row ==9 and col ==9:
                return
            elif col < 9 and row == 9:
                backtrack(col+1, row)
            else:
                backtrack(col, row+1)

        def backtrack(rol, col):
            if board[rol][col] == '.':
                box_idx = (rol // 3) * 3 + (col // 3)
                for num in range(1,10,1):
                    if is_available(rol, col, box_idx, num):
                        insert_num(rol, col, box_idx, num)
            else
                pass
