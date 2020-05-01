'''
输入一个正整数数组，把数组里所有数字拼接起来排成一个数，打印能拼接出的所有数字中最小的一个。
例如输入数组{3，32，321}，则打印出这三个数字能排成的最小数字为321323。
'''

from functools import cmp_to_key


class Solution:
    def build_minimum_number(self, numbers):
        if not numbers or len(numbers) <= 0:
            return ''

        numbers = [str(i) for i in numbers]
        # key是一种比较规则
        # 比较 x+y 和 y+x 的大小, 因为为str型, 需要先转换成int型
        numbers.sort(key=cmp_to_key(lambda x, y: int(x+y) - int(y+x)))
        return ''.join(numbers)


numbers = [3, 32, 321]
s = Solution()
print(s.build_minimum_number(numbers))