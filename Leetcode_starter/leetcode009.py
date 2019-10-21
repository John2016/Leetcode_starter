## 1009
## 回文数
## 要点是找到方法，都截取到中间，从后往前的数字要和从前往后的一样

class Solution:
    def isPalindrome(self, x: int) -> bool:
        reverse = 0
        while x > reverse:
            reverse = reverse * 10 + x % 10
            x = x // 10

        return(x == reverse or reverse // 10 == x)


if __name__ == '__main__':
    s = Solution()
    print(s.isPalindrome(12321))