# coding: utf-8


 # 青蛙跳台阶,每次可以跳1级或2级
'''
青蛙跳台阶:一只青蛙一次可以跳上1级台阶，也可以跳上2级。
求该青蛙跳上一个n级的台阶总共有多少种跳法（注意不是问总共跳了多少步）。
很多人喜欢正向思考，使用暴力求解，但往往这是一个很复杂的问题。
我们可以反过来思考：如果我们要跳上第 n 级台阶，该怎么跳？
当n很大时，青蛙在最后一步跳到第n级台阶时，有两种情况：
一种是青蛙从第n-1个台阶跳一个台阶，那么青蛙完成前面n-1个台阶，就有f(n-1)种跳法，
这是一个子问题。另一种是青蛙从第n-2个台阶跳两个台阶到第n个台阶，
那么青蛙完成前面n-2个台阶，就有f(n-2)种情况，这又是另外一个子问题。
我们令 f(n) 表示从第一级台阶跳上第 n 级台阶有几种跳法。则有如下递推公式：
f(n) = f(n-1) + f(n-2) 
然后通过实际的情况可以得出：只有一阶的时候 f(1) = 1 ,只有两阶的时候可以有 f(2) = 2
可以发现最终得出的是一个斐波那契数列：
        
       | 1, (n=1)
f(n) = | 2, (n=2)
       | f(n-1)+f(n-2) ,(n>2,n为整数)
'''
               
class Solution:
               
    def jumpFloor1(self, number): # 方法一
        res = [1, 2]  #resizable array
        while len(res) <= number:
            res.append(res[-1] + res[-2])
        # if number == 1:
        #     return 1
        # else:
        return res[number-1]
        
        
    def jumpFloor2(self, number): # 方法二
        res=[1,2] #resizable array
        if number >=3:
            for _ in range(number+1):
                res.append(res[-1]+res[-2])
        return res[number-1]
            
                  
    def jumpFloor3(self, number): #方法三
        res = [1, 2]  #resizable array
        if number >= 3:
            for i in range(3, number+1):
                res[(i+1)%2] = res[0] + res[1]
        return res[(number+1)%2]    
    
test = Solution()
# for i in range(8):
#     print(test.jumpFloor1(i))
# for i in range(8):
#     print(test.jumpFloor2(i))
print(test.jumpFloor1(4))
print(test.jumpFloor2(4))
print(test.jumpFloor3(4))
