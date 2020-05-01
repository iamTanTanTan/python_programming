'''
HZ偶尔会拿些专业问题来忽悠那些非计算机专业的同学。今天测试组开完会后,他又发话了:在古老的一维模式识别中,
常常需要计算连续子向量的最大和,当向量全为正数的时候,问题很好解决。但是,如果向量中包含负数,是否应该包含某个负数,
并期望旁边的正数会弥补它呢？例如:{6,-3,-2,7,-15,1,2,2},连续子向量的最大和为8(从第0个开始,到第3个为止)。
你会不会被他忽悠住？(子向量的长度至少是1)
'''
'''
思路一：对于连续子数组，可以用一个数值来存储当前和，如果当前和小于零，那么在进行到下一个元素的时候，
直接把当前和赋值为下一个元素，如果当前和大于零，则累加下一个元素，同时用一个max存储最大值并随时更新。

思路二：动态规划。设sum[i]为以第i个元素结尾的最大的连续子数组的和。假设对于元素i，
所有以它前面的元素结尾的子数组的长度都已经求得，那么以第i个元素结尾且和最大的连续子数组实际上，
要么是以第i-1个元素结尾且和最大的连续子数组加上这个元素，要么是只包含第i个元素，即sum[i]
'''


class Solution:
    # 方法一
    def get_maximum_sum(self, array):
        if not array or len(array) <= 0:
            return 0

        sum = 0
        max = array[0]
        for i in range(len(array)):
            if sum <= 0:
                sum = array[i]
            else:
                sum += array[i]

            if sum > max:
                max = sum

        return max

    # 方法二

    def get_maximum_sum2(self, array):
        if not array or len(array) <= 0:
            return 0
        # 注意这里range从1开始，如果从0开始，则第一项变为max(array[0]  + array[-1], array[0])
        for i in range(1, len(array)):
            # 当前值的大小与前面的值之和比较，取大者
            sub_max = max(array[i] + array[i-1], array[i])
            # 将当前和的最大值sub_max赋给array[i],新的array存储的为所有sub_max的值
            array[i] = sub_max

        return max(array)


array = [1, -2, 3, 10, -4, 7, 2, -5]
s = Solution()
print(s.get_maximum_sum(array))
print(s.get_maximum_sum2(array))
