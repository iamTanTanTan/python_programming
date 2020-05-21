'''
题目：给定一个数组和滑动窗口的大小，找出所有滑动窗口里数值的最大值。例如，如果输入数组{2,3,4,2,6,2,5,1}及
滑动窗口的大小3，那么一共存在6个滑动窗口，他们的最大值分别为{4,4,6,6,6,5}； 针对数组{2,3,4,2,6,2,5,1}的
滑动窗口有以下6个： {[2,3,4],2,6,2,5,1}， {2,[3,4,2],6,2,5,1}， {2,3,[4,2,6],2,5,1}，
{2,3,4,[2,6,2],5,1}， {2,3,4,2,[6,2,5],1}， {2,3,4,2,6,[2,5,1]}。
'''


class Solution:
    # k 为滑窗尺寸
    def max_in_window(self, nums, k):
        if k <= 0 or len(nums) < k:
            return []

        n = len(nums) - k + 1
        ans = []
        for i in range(n):
            slide_win = nums[i:i+k]
            ans.append(max(slide_win))
        return ans


test = [2, 3, 4, 2, 6, 2, 5, 1]
s = Solution()
print(s.max_in_window(test, 3))
