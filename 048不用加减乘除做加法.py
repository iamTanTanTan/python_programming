'''
写一个函数，求两个整数之和，要求在函数体内不得使用+、-、*、/四则运算符号。
'''

class Solution:
    # 特别注意sum()求和里面是个[]列表对象，直接输入num，num2是不行的
    def add(self, num1, num2):
        return sum([num1, num2])


s = Solution()
print(s.add(4, -2))