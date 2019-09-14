/*
 * leetcode 003
 * low time complexity and a little high space occupation
 * 找出字符串中最长无重复子串
 * 要点是：1. 设计算法避免重复无意义的序列比对
 *        2. 利用字符的有限性构造数组实现最快的字符比对
 * 不同方法主要体现在“剪枝算法”与所设计数据结构的不同
 */

#include <string>
#include <iostream>

using namespace std;

class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        // initialize the random-get array
        const int MAX_CHARS = 256;
        int array[MAX_CHARS];
        memset(array, -1, sizeof(array));
        
        int max_len = 0;
        int last_repeat_pos = -1;

        for (int i = 0; i < s.size(); i++)
        {
            /* code */
            if (array[s[i]] != -1 && last_repeat_pos < array[s[i]])
            {
                last_repeat_pos = array[s[i]];
            }
            if (i - last_repeat_pos > max_len)
            {
                max_len = i - last_repeat_pos;
            }
            array[s[i]] = i;
            
        }
        return max_len;   
    }
};