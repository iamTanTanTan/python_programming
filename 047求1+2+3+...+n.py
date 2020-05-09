'''
求1+2+3+...+n，要求不能使用乘除法、for、while、if、else、switch、case等关键字及条件判断语句（A?B:C）。
'''

class Solution:
    #方法一
    def sum_solution1(self, n):
        return sum(range(1, n+1))

    
    #方法二
    def sum_solution2(self, n):
        # a and b, 若a为False，返回a, 若a为True，返回b
        return n and (n + self.sum_solution2(n-1))

s = Solution()
print(s.sum_solution1(100))
print(s.sum_solution2(100))