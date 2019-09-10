/*
    2019/9/10
    Sum of two numbers
*/

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> ii_map;
        vector<int> result;
        for (int i = 0; i < nums.size(); i++)
        {
            /* check */
            if (ii_map.find(nums[i]) == ii_map.end())
            {
                /* insert */
                ii_map[target-nums[i]] = i;
            }
            else
            {
                /* collect result */
                result.push_back(ii_map[nums[i]]);
                result.push_back(i);
                break;
            }
        }
    return result;
    }
};