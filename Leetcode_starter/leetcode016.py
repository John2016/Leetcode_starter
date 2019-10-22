## 1016
## 三数之和，求一个数组中所有三数之和与目标数字差异最小的可能
## 重点是先排序，及使用双指针，并在之前的基础上加入对比差异

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
    ##def threeSum(self, nums):
        nums.sort()

        # res = []
        ii = 0
        diff = 2147483647

        for ii in range(0, len(nums) - 2, 1):
            if nums[ii] > 0:
                return([nums[0], nums[1], nums[2] ])

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
                    res.append( [ nums[ii], nums[jj], nums[kk] ] )
                    jj += 1
                    kk -= 1
                    while jj < kk and nums[jj + 1] == nums[jj]:
                        jj += 1
                    while jj < kk and nums[kk - 1] == nums[kk]:
                        kk -= 1

        return res


if __name__ == '__main__':
    s = Solution()
    print(s.threeSum([-2,-1,0,1,2]))