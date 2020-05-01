'''
请实现一个函数用来找出字符流中第一个只出现一次的字符。例如，当从字符流中只读出前两个字符"go"时，
第一个只出现一次的字符是"g"。当从该字符流中读出前六个字符“google"时，第一个只出现一次的字符是"l"。
'''

'''
思路：先遍历一遍字符串，用一个hash表存放每个出现的字符和字符出现的次数。
再遍历一遍字符串，找到hash值等于1的输出即可。
'''


class Solution:
    def first_once_char(self, s):
        if len(s) <= 0:
            return -1
        # 存储每个出现的字符和字符出现的次数
        adict = {}
        # 存储字符串中所有字符
        alist = list(s)

        for i in alist:
            if i not in adict.keys():
                adict[i] = 0
            adict[i] += 1

        for j in alist:
            if adict[j] == 1:
                return j

        # 如果没有符合要求的字符，返回-1
        return -1


s = Solution()
print(s.first_once_char('abaccdeff'))
