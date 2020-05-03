'''
输入一个递增排序的数组和一个数字S，在数组中查找两个数，使得他们的和正好是S，
如果有多对数字的和等于S，输出两个数的乘积最小的。

对应每个测试案例，输出两个数，小的先输出。
'''

'''
思路：
数列满足递增，设两个头尾两个指针i和j，
若ai + aj == sum，就是答案（相差越远乘积越小）
若ai + aj > sum，aj肯定不是答案之一（前面已得出 i前面的数已是不可能），j -= 1
若ai + aj < sum，ai肯定不是答案之一（前面已得出 j后面的数已是不可能），i += 1
'''


class Solution:
    # 从左右一起查找
    # 因为当两个数的和一定的时候, 两个数字的间隔越大, 乘积越小
    # 所以直接输出查找到的第一对数即可
    def find_nums_with_sum(self, array, sum):
        if not array:
            return []

        left = 0
        right = len(array) - 1

        while left < right:
            if array[left] + array[right] < sum:
                left += 1
            elif array[left] + array[right] > sum:
                right -= 1
            else:
                return [array[left], array[right]]

        return []


test = [1, 2, 4, 7, 11, 15]
s = Solution()
print(s.find_nums_with_sum(test, 15))
