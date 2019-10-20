## leetcode 1005
## 最长回文子串

class Solution:
    def longestPalindrome(self, s: str) -> str:
        str_len = len(str)

        if str_len <= 1:
            return s
        cal_matrix = [ [ False for _ in range(str_len)] for _ in range(str_len) ]

        longest_num = 1
        longest_str = ''

        for ii in range(0, str_len, 1):
            for jj in range(0, ii+1, 1):
                if s[ii] == s[jj] and (ii - jj <= 2 or cal_matrix[jj + 1][ii - 1]):
                    cal_matrix[jj][ii] = True
                    if ii - jj + 1 > longest_num:
                        longest_num = ii - jj + 1
                        longest_str = s[jj:ii+1]

        return longest_str


tmp = 'babad'
aaa = Solution()
print(aaa.longestPalindrome(tmp))