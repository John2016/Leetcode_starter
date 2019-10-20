/*
 * leetcode 1009
 * 不将整数转为字符串来判断一个整数是不是回文数
 * 要点是找技巧，经典方法是通过除法与求余将数字从尾部依次倒转，只截一半
 */

class Solution {
public:
    bool isPalindrome(int x) {
        int ans = 0;
        int cur;
        while(x > ans)
        {
            cur = x % 10;
            ans = ans * 10 + cur;
            x = x / 10;
        }
        return ans == x || ans == x * 10
    }
};