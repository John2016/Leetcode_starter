"""
   This is the custom function interface.
   You should not implement it, or speculate about its implementation
   class CustomFunction:
       # Returns f(x, y) for any given positive integers x and y.
       # Note that f(x, y) is increasing with respect to both x and y.
       # i.e. f(x, y) < f(x + 1, y), f(x, y) < f(x, y + 1)
       def f(self, x, y):
  
"""
class Solution(object):
    def findSolution(self, customfunction, z):
        """
        :type num: int
        :type z: int
        :rtype: List[List[int]]
        """
        res = []
        
        for ii in range(1,1001,1):
            left = 1
            right = 1000
            while left <= right:
                if customfunction.f(ii, left) > z or customfunction.f(ii, right) < z:
                    break
                median = (left + right) // 2
                if customfunction.f(ii, median) > z:
                    right = median - 1
                elif customfunction.f(ii, median) < z:
                    left = median + 1
                else:
                    res.append([ii,median])
                    break
        return res
        
