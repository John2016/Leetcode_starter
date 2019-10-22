## leetcode 1036
## 解数独
## 思路是利用map，并且定义行、列、格子的map list


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # init three maps
        

        # validate
        for ii in range(9):
            for jj in range(9):
