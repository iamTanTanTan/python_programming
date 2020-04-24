# coding: utf-8

'''
在一个二维数组中（每个一维数组的长度相同），每一行都按照从左到右递增的顺序排序，
每一列都按照从上到下递增的顺序排序。请完成一个函数，输入这样的一个二维数组和一个整数，
判断数组中是否含有该整数。
'''

#方法一： 循环迭代查找，不是最优

class Solution:
    # array 二位列表
    def find(self, target, array):
       
        if not array:
            return
        row = len(array)
        col = len(array[0])
        
        for i in range(row):
            for j in range(col):
                if target == array[i][j]:
                    return True
        return False
    
# =============================================================================
# array = [[1, 2, 8, 9],
#          [2, 4, 9, 12],
#          [4, 7, 10, 13],
#          [6, 8, 11, 15]]
# =============================================================================
array = [[1, 2, 8, 9],
         [2, 4, 9, 12],
         [4, 7, 10, 13],
         [6, 8, 11, 15],
         [7, 9, 12, 17]]

findtarget = Solution()
    
print(findtarget.find(4,array))

# =============================================================================
# 方法二： 上述方法的时间复杂度是O(n^2)，最优化的方式是从左下或者右上开始搜索
# 从右上开始搜索，如果数组中的数比该数要大，那么向左移动一位，如果数组中的数比该数小，向下移动一位，
# 因为数组本身是从左到右依次增大，从上到下一次增大
# =============================================================================

class Solution:
    # 二维列表
    def find(self, target, array):
        if not array:
            return
        row = len(array)
        col = len(array[0])
        
        i = 0
        j = col - 1
        while i < row and j >= 0:
            if target < array[i][j]:
                j -= 1
            elif array[i][j] < target:
                i += 1
            else:
                return True
        return False
        
array = [[1, 2, 8, 9],
         [2, 4, 9, 12],
         [4, 7, 10, 13],
         [6, 8, 11, 15],
         [7, 9, 12, 17]]

findtarget = Solution()
    
print(findtarget.find(4,array))


