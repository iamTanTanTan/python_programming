'''
请实现一个函数用来判断字符串是否表示数值（包括整数和小数）。
例如，字符串"+100","5e2","-123","3.1416"和"-1E-16"都表示数值。 
但是"12e","1a3.14","1.2.3","+-5"和"12e+4.3"都不是。
'''

import re


class Solution:
    # 方法一：利用float强转
    def is_numeric1(self, s):
        try:
            return float(s)
        except:
            return None

    # 方法二：正则表达式

    def is_numeric2(self, s):
        if not s:
            return None

        # 正则表达式，*匹配前一个字符出现任意次（包括0次）
        # ？匹配前一个字符出现0次或1次，+匹配前一个字符出现至少1次
        p = re.compile(r'^[\+\-]?\d*(\.\d+)?([eE][\+\-]?\d+)?$')
        return p.match(s)


s = Solution()
print(s.is_numeric1('12e5'))
print(s.is_numeric1('-1E-16'))
print(s.is_numeric1('12e+4.3'))
print(s.is_numeric2('12e5'))
print(s.is_numeric2('-1E-16'))
print(s.is_numeric2('12e+4.3'))
