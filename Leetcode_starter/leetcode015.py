## 1015
## 三数之和，求一个数组中所有三数之和为0的可能
## 重点是先排序，及使用双指针

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        res = []
        ii = 0

        for ii in range(0, len(nums) - 2, 1):
            if nums[ii] > 0:
                break

            jj = ii + 1
            kk = len(nums) - 1

            while jj < kk:
                sum = nums[ii] + nums[jj] + nums[kk]

                if sum > 0:
                    kk -= 1
                    while nums[kk-1] == nums[kk] and jj < kk:
                        kk -= 1
                elif sum < 0:
                    jj += 1
                    while nums[jj + 1] == nums[jj] and jj < kk:
                        jj += 1
                else:
                    res.append([nums[ii], nums[jj], nums[kk] ] )

        return res