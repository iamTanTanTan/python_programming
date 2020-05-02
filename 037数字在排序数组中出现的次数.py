'''
统计一个数字在排序数组中出现的次数。
'''

from bisect import bisect_left, bisect_right


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
            # 定位目标元素在[lo:]中的右边界
            hi = bisect_right(nums[lo:], k)
            return hi

        else:
            return 0

        return hi


s = Solution()
print(s.number_of_k1([1, 3, 3, 4, 5], 3))
print(s.number_of_k2([1, 3, 3, 4, 5], 3))
print(s.number_of_k1([], 1))
print(s.number_of_k2([], 1))
