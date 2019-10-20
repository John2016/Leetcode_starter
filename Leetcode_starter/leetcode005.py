## leetcode 1005
## 最长回文子串

class Solution:
    def longestPalindrome(self, s: str) -> str:
        str_len = len(str)
        cal_matrix = [ [ [0] * ii] for ii in range(str_len, 0 ,-1) ]

        for ii in range(0, str_len, 1):
            cal_matrix[0][ii] = 1
            cal_matrix[ii][0] = 1

        for ii in range(1, str_len - 1, 1)