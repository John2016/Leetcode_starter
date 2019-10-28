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
            return not (row_map[row][num] or col_map[col][num] or box_map[box_index][num])

        def insert_num(row, col, box, num):
            row_map[row][num] = True
            col_map[col][num] = True
            box_map[box][num] = True
            board[row][col] = str(num)


        def remove_num(row, col, box, num):
            row_map[row][num] = False
            col_map[col][num] = False
            box_map[box][num] = False
            board[row][col] = '.'
        
        def add_next(row, col):
            if row == 8 and col == 8:
                nonlocal solved
                solved = True
            elif col == 8:
                backtrack(row + 1, 0)
            else:
                backtrack(row, col + 1)


        def backtrack(row=0, col=0):
            if board[row][col] == '.':
                box_idx = (row // 3) * 3 + (col // 3)
                for num in range(1,10,1):
                    if is_available(row, col, box_idx, num):
                        insert_num(row, col, box_idx, num) 
                        add_next(row, col)
                        if not solved:
                            remove_num(row, col, box_id, num)            
            else:
                add_next(row, col)

        row_map = [[False for _ in range(1,10) ] for _ in range(9)]
        col_map = [[False for _ in range(1,10) ] for _ in range(9)]
        box_map = [[False for _ in range(10)] for _ in range(9)]

        for ii in range(9):
            for jj in range(9):
                box_id = (ii // 3) * 3 + (jj // 3)
                if board[ii][jj] != '.':
                    dd = int(board[ii][jj])
                    insert_num(dd,ii,jj,box_id)
        
        solved = False
        backtrack()

