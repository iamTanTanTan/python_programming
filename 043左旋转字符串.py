'''
汇编语言中有一种移位指令叫做循环左移（ROL），现在有个简单的任务，就是用字符串模拟这个指令的运算结果。
对于一个给定的字符序列S，请你把其循环左移K位后的序列输出。例如，字符序列S=”abcXYZdef”,要求输出循环左移3位后
的结果，即“XYZdefabc”。是不是很简单？OK，搞定它
'''

'''
思路一：使用python切片操作

思路二：对原字符串进行扩充两倍，在这个基础上直接从要反转的地方取就可以，相当于前n个字符串翻转了
'''


class Solution:
    # 方法一
    def left_rotate_string1(self, s, n):
        return s[n:] + s[0:n]

    # 方法二

    def left_rotate_string2(self, s, n):
        if not s:
            return ''

        length = len(s)
        s += s

        return s[n:length+n]


s = Solution()
print(s.left_rotate_string1('abcdefg', 2))
print(s.left_rotate_string2('abcdefg', 2))
