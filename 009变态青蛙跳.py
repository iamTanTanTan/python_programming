# coding: utf-8

'''
题目：一只青蛙一次可以跳上1级台阶，也可以跳上2级……它也可以跳上n级。
求该青蛙跳上一个n级的台阶总共有多少种跳法
'''

'''
当n很大时，青蛙在最后一步跳到第n级台阶时，可以分成以下情况：
青蛙从第n-1个台阶跳1个台阶到达第n个台阶，那么青蛙完成前面n-1个台阶，就有f(n-1)种跳法
青蛙从第n-2个台阶跳2个台阶到第n个台阶，那么青蛙完成前面n-2个台阶，就有f(n-2)种跳法
......
青蛙从第1个台阶跳n-1个台阶到第n个台阶，那么青蛙完成前面1个台阶，就有f(1)种跳法
青蛙从第0个台阶跳n个台阶到第n个台阶，那么青蛙完成前面0个台阶，就有f(0)种跳法

所以f(n)=f(n-1)+f(n-2)+...+f(1)+f(0)
由于f(0) 表示青蛙在地上，所以f(0)=0
f(n)=f(n-1)+f(n-2)+...+f(1)
由于        f(n-2)+...+f(1)=f(n-1)
可以得出：
f(n) = 2*f(n-1)
'''
class Solution:
    def jumpFloor(self, number):
        ans = 1
        if number >= 2:
            for i in range(number-1):
                ans = ans * 2
        return ans
        
test = Solution()
print(test.jumpFloor(8))
