# coding: utf-8


class Solution:
    '''
    二进制表示中：奇数末尾数字为1，偶数末尾数字为0.
    数字1的前面N位均为0，末尾数字为1。跟它做与运算，奇数为1(True)，偶数为0(False)。
    '''
    def reorderOddEven1(self, array):
        left = [x for x in array if x & 1] # 奇数： x & 1 = True
        right = [x for x in array if not x & 1] # 偶数： not x & 1 = True
        return left + right
    
    def reorderOddEven2(self, array):
        if len(array) < 0:
            return []
        if len(array) == 1:
            return array
        arrayOdd = []
        arrayEven = []
        for num in array:
            if num & 0x1:
                arrayOdd.append(num)
            else:
                arrayEven.append(num)
        return arrayOdd + arrayEven
    
        
S = Solution()

print(S.reorderOddEven1([12, -1, 2, -3, 4, -5, -6, 7, 8, 9, 10, -10]))
print(S.reorderOddEven2([12, -1, 2, -3, 4, -5, -6, 7, 8, 9, 10, -10]))