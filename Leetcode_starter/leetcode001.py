## leetcode 1001
## 两数之和，求数组中和为给定数的两个数
## 要点是熟练使用mao数据结构

class Solution:
    ## def twoSum(self, nums: List[int], target: int) -> List[int]:
    def twoSum(self, nums, target):
        table = {}
        for ii,num in enumerate(nums):
            xx = table.get(num)
            if xx is not None:
                return [xx, ii]
            
            table[target-num] = ii

        return None

if __name__ == '__main__':
    s = Solution()
    print(s.twoSum([3,3],6))
            