'''
0,1,…,n-1这n个数字排成一个圆圈， 从数字0开始每次从这
个圆圈里删除第m个数字。 求出这个圆圈里剩下的最后一个数字。
'''
'''
思路：约瑟夫环问题,具体参考维基百科
递推公式：f(n, m) = [f(n-1, m) + m] % n
         f(1, m) = 0
'''


class Solution:
    # n表示元素总数
    def last_remaining(self, n, m):
        if n < 1 or m < 1:
            return -1
        # 只有一个人时，index 0就是最后剩下的
        remain_index = 0
        for i in range(1, n+1):
            remain_index = (remain_index + m) % i

        return remain_index


s = Solution()
print(s.last_remaining(5, 3))
