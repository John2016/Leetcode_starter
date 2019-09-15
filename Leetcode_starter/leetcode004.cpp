/*
 * leetcode 004
 * 找到两个有序数组的中位数，需要O(log(m+n))的复杂度
 * 要点是通过不断对比两个数组的中位数并不断二分，需要注意临界条件和记述
 * 注意有一种网上流行的方法其复杂度是O(m+n)
 */
#include<math.h>
#include<vector>

using namespace std;

class Solution {
public:
    double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) {
        int len_1 = nums1.size();
        int len_2 = nums2.size();

        // 处理偶数个数字序列的中位数，鲁棒
        int left = (len_1 + len_2 + 1) / 2;
        int right = (len_1 + len_2 + 2) / 2;

        return (get_k(nums1, 0, len_1-1, nums2, 0, len_2-1, left) + get_k(nums2, 0, len_1-1, nums2, 0, len_2-1, right)) * 0.5;

    }

private:
    int get_k(vector<int>& num_1, int head_1, int tail_1, vector<int>& num_2, int head_2, int tail_2, int kk) {
        int len_1 = tail_1 - head_1 + 1;
        int len_2 = tail_2 - head_2 + 1;

        if(len_1 > len_2) return get_k(num_2, head_2, tail_2, num_1, head_1, tail_1, kk);
        
        if(len_1 == 0)    return num_2[head_2 + kk - 1];
        if(kk == 1)       return Math.min(num_1[head_1], num_2[head_2]);

        // 这里的处理是为了避免溢出，但是一般的kk
        int ii = head_1 + Math.min(len_1, kk / 2) - 1;
        int jj = head_2 + Math.min(len_2, kk / 2) - 1;

        if(num_1[ii] > num_2[jj]) {
            return get_k(num_1, head_1, tail_1, num_2, jj + 1, tail_2, kk - (jj - head_2 + ii));
        }
        else{
            return get_k(num_1, ii + 1, tail_1, num_2, head_2, tail_2, kk - (ii - head_1 + 1));
        }
    }
};

