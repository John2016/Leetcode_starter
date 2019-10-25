## leetcode 1003
## 找出字符串种最长的无重复子串

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0

        bool_array = [-1 for i in range(256)]
        last_occur_pos = -1
        res = 0
        
        for ii, ch in enumerate(s):
            if bool_array[ord(ch)] != -1 and last_occur_pos < bool_array[ord(ch)]:
                last_occur_pos = bool_array[ord(ch)]
            if (ii - last_occur_pos > res):
                res = ii - last_occur_pos
            bool_array[ord(ch)] = ii

        return res

if __name__ == '__main__':
    s = Solution()
    print(s.lengthOfLongestSubstring('abba'))