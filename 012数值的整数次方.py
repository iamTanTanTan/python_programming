# coding: utf-8

'''
给定一个double类型的浮点数base和int类型的整数exponent。求base的exponent次方
'''


class Solution:
    # 方法一
    def power1(self, base, exponent): 
        # write code here
        return base**exponent

    # 方法二
    def power2(self, base, exponent):
        if exponent == 0:
            return 1
        elif exponent == 1:
            return base
        
        result = 1
        for _ in range(abs(exponent)):
            if exponent < 0:
                result = 1 / (result * base)
            else:
                result = result * base
            
        return result

test = Solution()
print(test.power1(0, 0))
print(test.power1(-2, 1))
print(test.power1(2, 5))
print(test.power1(-2, -1))
print(test.power2(0, 0))
print(test.power2(-2, 1))
print(test.power2(2, 5))
print(test.power2(-2, -1))
