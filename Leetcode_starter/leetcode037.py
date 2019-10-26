## leetcode 37
## 解数独
## 基于第36题，加入回溯

class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        def is_available(row, col, box, num):
            # box_index = (row // 3) * 3 + col//3
            return not (rol_map[row][num] or col_map[col][num] or box_map[box_index][num])

        def insert_num(row, col, box, num):
            rol_map[row][num] = True
            col_map[col][num] = True
            box_map[box][num] = True


        def remove_num():
            rol_map[row][num] = False
            col_map[col][num] = False
            box_map[box][num] = False
        
        def add_next():


        def backtack(rol, col):

