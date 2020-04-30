'''
输入n个整数，找出其中最小的K个数。例如输入4,5,1,6,2,7,3,8这8个数字，则最小的4个数字是1,2,3,4,。
'''

'''
思路一：这一题应用堆排序算法复杂度只有O(nlog k)，堆是完全二叉树的一种，最大堆就是最上面的数是最大的
该方法基于二叉树或者堆来实现，首先把数组前k个数字构建一个最大堆，然后从第k+1个数字开始遍历数组，如果遍历到的
元素小于堆顶的数字，那么久将换两个数字，重新构造堆，继续遍历，最上面的k个数即为最大值，时间复杂度O(nlog k)。
这里我们使用最大堆的思想，不过构造最小堆。

思路二 ：排序
'''

# 方法一

class Solution1:
    def get_least_numbers1(self, k, input):
        import heapq
        if input == None or len(input) < k or len(input) <= 0 or k < 0:
            return []

        # 建立最小堆，最上面那个数是最小的，返回一个列表，这个列表就是从最小值开始的k个数
        return heapq.nsmallest(k, input)


# 方法二

class Solution2:
    def get_least_numbers2(self, k, input):
        if input == None or len(input) < k or len(input) <= 0 or k <= 0:
            return []
        # 使用python内置排序函数
        return sorted(input)[:k]


input = [4, 5, 1, 6, 2, 7, 3, 8]
S1 = Solution1()
S2 = Solution2()
print(S1.get_least_numbers1(4, input))
print(S1.get_least_numbers1(5, input))
print(S2.get_least_numbers2(4, input))
print(S2.get_least_numbers2(5, input))
