# coding: utf-8

'''
给定一个double类型的浮点数base和int类型的整数exponent。求base的exponent次方
'''
'''
和C，C++ 等语言不一样，python内置了求幂运算符**，可以直接实现

class Solution:
    def Power(self, base, exponent=2): # 默认输出二次方结果
        # write code here
        return base**exponent
    
test = Solution()
print(test.Power(0, 0))
print(test.Power(-2, 4))
print(test.Power(-2, 5))
print(test.Power(-2, -1))
print(test.Power(9))
