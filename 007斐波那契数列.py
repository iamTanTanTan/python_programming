# coding: utf-8

'''要求输入一个整数n，请你输出斐波那契数列的第n项（从0开始，第0项为0）。'''    

class Solution:
    #斐波那契数列
    def Fibonacci1(self, n): #方法一
        res = [0, 1] #resizable array
        if n >= 2:
            for i in range(2, n+1):
                res[i%2] = res[0] + res[1] #奇偶交替相加
        return res[n%2]
    
    def Fibonacci2(self, n): #方法二
        a=0
        b=1
        if n == 0:
            return a
        elif n == 1:
            return b
        for _ in range(n-1):
            a, b = b, a + b
        return b  
   
        
    
test = Solution()
print(test.Fibonacci1(8))
print(test.Fibonacci2(8))




