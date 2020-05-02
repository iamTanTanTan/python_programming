'''
在数组中的两个数字如果前面一个数字大于后面的数字， 则这两个数字组成一个逆序对。
输入一个数组， 求出这个数组中的逆序对的总数。
'''
'''
思路：
    index   0       1       2
    data    9       8       7
    copy    7       8       9
    逆序数  2   +   1   +   0
'''


class Solution:
    # 使用数据的index求解
    def inversion_count(self, data):
        if len(data) <= 0:
            return 0

        copy = []
        for i in range(len(data)):
            copy.append(data[i])
        copy.sort()

        j = 0
        count = 0
        while j < len(copy):
            count += data.index(copy[j])
            data.remove(copy[j])
            j += 1

        return count


s = Solution()
print(s.inversion_count([7, 8, 9]))
print(s.inversion_count([9, 8, 7]))
print(s.inversion_count([5, 2, 9, 1, 0, 4]))
