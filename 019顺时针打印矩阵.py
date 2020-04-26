# coding: utf-8

'''
输入一个矩阵，按照从外向里以顺时针的顺序依次打印出每一个数字，
例如，如果输入如下矩阵：
[[ 1,  2,  3,  4],
 [ 5,  6,  7,  8],
 [ 9, 10, 11, 12],
 [13, 14, 15, 16]]
则依次打印出数字 1,2,3,4,8,12,16,15,14,13,9,5,6,7,11,10.
'''
'''
思路
1. 先将矩阵第一行的值另外存起来，然后删掉第一行。
2. 矩阵逆时针旋转 90°，再存第一行的值，再删掉。
3. 直到矩阵为空时，停止。
'''

class Solution:
    def printMatrixClockwise(self, matrix):      
        if not matrix:
            return matrix
        res = []
        while matrix:
            #取第一行存入res同时消除matrix第一行
            res += matrix.pop(0)
            # res.extend(matrix[0])
            # matrix.remove(matrix[0])
            
            tmp = []
            tmp2 = []
            if matrix:
                row = len(matrix)
                col = len(matrix[0])
                #矩阵逆时针旋转90度
                for j in range(col):
                    for i in range(row):
                        tmp.append(matrix[i][col - 1 - j])
                    tmp2.append(tmp)
                    tmp = []
                matrix = tmp2
        print(res)
        return res
        

matrix = [[1,  2,  3,  4],
          [5,  6,  7,  8],
          [9, 10, 11, 12],
          [13, 14, 15, 16]]
matrix2 = [[1],[2],[3],[4],[5]]
matrix3 = [[1,2],[3,4],[5,6],[7,8],[9,10]]
S = Solution()
S.printMatrixClockwise(matrix)
S.printMatrixClockwise(matrix2)
S.printMatrixClockwise(matrix3)