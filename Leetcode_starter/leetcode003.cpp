/*
 * low time complexity and a little high space occupation
 * Yuan
 * 12th Sep 2019
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