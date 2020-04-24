# coding: utf-8

'''
我们可以用 2 * 1 的小矩形横着或者竖着去覆盖更大的矩形。
请问用n个2 * 1的小矩形无重叠地覆盖一个2*n的大矩形，总共有多少种方法？
'''

'''
把覆盖2*n矩形的覆盖方法总数记为f(n).用第一个矩形去覆盖大矩形时，有两种选择，横放或者竖放。
竖放时，右边有2*(n-1)的区域尚未被覆盖，那么剩下区域覆盖方法的总数为f(n-1)。
第一个矩形横向的情况下，必须占用另外一个小矩形去覆盖左下角.
因此右边还剩下2*(n-2)的区域尚未被覆盖，记为f(n-2)。因此可以得出关系，
f(n) = f(n-1) + f(n-2)。显然我们也知道f(1)=1,f(2) = 2.
'''

class Solution:
    def vectCover1(self, number): # 方法一
        a = 1
        b = 2
        if number == 1:
            return a
        if number == 2:
            return b
        for _ in range(number-2):
            a, b = b, a + b
        return b
    
    def vectCover2(self, number): # 方法二
        res = [1, 2] #resizable array
        while len(res) <= number:
            res.append(res[-1] + res[-2])
        return res[number-1]
    
    def vectCover3(self, number): # 方法三
        res = [1, 2] #resizable array
        if number >= 3:
            for i in range(3, number+1):
                res[(i+1)%2] = res[0] + res[1]
        return res[(number+1)%2]
    

        
test = Solution()
print(test.vectCover1(4)) 
print(test.vectCover2(4))  
print(test.vectCover3(4))   
# for i in range(8):
#     print(test.vectCover2(i))         
 
