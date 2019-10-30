## 1004
## 两个有序数组的中位数，要求时间复杂度
## 要点是

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        num_1 = nums1.len()
        num_2 = nums2.len()

        left = (num_1 + num_2 + 1) / 2
        right = (num_1 + num_2 + 2) / 2
        