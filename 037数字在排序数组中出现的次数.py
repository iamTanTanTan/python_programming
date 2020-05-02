'''
统计一个数字在排序数组中出现的次数。
'''

from bisect import bisect_left


class Solution:

    # 方法一，使用count函数顺序查找

    def number_of_k1(self, nums, k):
        return nums.count(k)

    # 方法二，使用标准库二分查找函数bisect

    def number_of_k2(self, nums, k):
        if not nums:
            return 0

        # 定位目标元素可能的最左侧位置
        lo = bisect_left(nums, k)
        # 若目标元素在nums中存在
        if k in nums[lo:lo+1]:
            # 当nums[lo]等于目标元素，则依次循环判断
            # 直到nums[lo]不等于目标元素时，循环结束
            count = 0
            while nums[lo] == k:
                count += 1
                lo += 1
            return count

        else:
            return 0


s = Solution()
print(s.number_of_k1([1, 3, 3, 4, 5], 3))
print(s.number_of_k2([1, 3, 3, 4, 5], 3))
print(s.number_of_k1([], 1))
print(s.number_of_k2([], 1))
