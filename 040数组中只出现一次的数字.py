'''
一个整型数组里除了两个数字之外，其他的数字都出现了两次。请写程序找出这两个只出现一次的数字。
'''

'''
思路一：利用python自带的counter库

思路二：异或运算
'''




from collections import Counter
class Solution:
    def once_appeared_num(self, array):
        # 返回一个列表，map（f,input）,对input进行f操作，第一个参数lambda函数，意思取返回值中的第一个数，因为counter函数返回的是字典，
        # counter（）.most_common返回的是有序的计数字段，顺序从大到小。取最后两个。
        return list(map(lambda c: c[0], Counter(array).most_common()[-2:]))


array = [2, 4, 3, 6, 3, 2, 5, 5]
s = Solution()
print(s.once_appeared_num(array))
