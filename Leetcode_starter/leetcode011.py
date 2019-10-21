## 1011
## 盛水最多的容器
## 要点是双指针

class Solution:
    ## def maxArea(self, height: List[int]) -> int:
    def maxArea(self, height):
        max_water = 0

        num_pillar = len(height)
        left = 0
        right = num_pillar - 1

        while left < right:
            current_water = min(height[left], height[right]) * (right - left)
            max_water = max(current_water, max_water)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        
        return max_water


if __name__ == '__main__':
    s = Solution()
    print(s.maxArea([1,8,6,2,5,4,8,3,7]))

            

