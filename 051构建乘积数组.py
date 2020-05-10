'''
给定一个数组A[0,1,...,n-1],请构建一个数组B[0,1,...,n-1],其中B中的元素
B[i]=A[0]*A[1]*...*A[i-1]*A[i+1]*...*A[n-1]。不能使用除法
'''

'''
思路一：
使用functools标准库中的reduce函数

思路二：
        B[0] = A[1] * A[2] * A[3] * A[4] *....*A[n-1] ;（没有A[0]）
        B[1 ]= A[0] * A[2] * A[3] * A[4] *....*A[n-1] ;（没有A[1]）
        B[2] = A[0] * A[1] * A[3] * A[4] *....*A[n-1] ;（没有A[2]）
举例：   输入：  1   2  3  4  5
        输出：  120 60 40 30 24
相当于一个矩形，被省去的那个数字设为1，1刚好在从左上到右下的对角线上，可以先算下三角中的连乘，
即我们先算出B[i]中的一部分，然后倒过来按上三角中的分布规律，把另一部分也乘进去。
'''



from functools import reduce

class Solution:

    # 方法一
    def multiply1A(self, A):
        if not A:
            return []

        B = []
        for i in range(len(A)):
            temp = A[i]
            A[i] = 1
            B.append(reduce(lambda x, y: x*y, A))
            A[i] = temp

        return B

    
    # 方法一改进
    def multiply1B(self, A):
        if not A:
            return []

        B =[]
        for i in range(len(A)):
            B.append(reduce(lambda x, y: x*y, (A[:i] + A[i+1:])))

        return B


    # 方法二
    def multiply2(self, A):
        if not A:
            return 0

        length = len(A)
        B = [1] * length

        # 下三角，B[0] = 1, 从1开始乘，
        for i in range(1, length):
            B[i] = B[i-1] * A[i-1]

        # 上三角，接着下三角从大往小乘，再与之前计算好的相乘
        temp = 1
        for i in range(length-2, -1, -1):
            temp = temp * A[i+1]
            B[i] *= temp

        return B


test = [1, 2, 3, 4]
s = Solution()
print(s.multiply1A(test))
print(s.multiply1B(test))
print(s.multiply2(test))
