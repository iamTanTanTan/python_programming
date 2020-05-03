'''
从扑克牌中随机抽5张牌， 判断是不是一个顺子， 即这5张牌是不是连续的。
2～ 10为数字本身， A为1， J为11， Q为12， K为13， 而大、小王可以看成任意数字。
'''
'''
思路：先统计王的数量，再把牌排序，如果后面一个数比前面一个数大于1以上，那么中间的差值就必须用王来补了。
看王的数量够不够，如果够就返回true，否则返回false。
'''


class Solution:
    def is_continuous(self, nmubers):
        if not nmubers:
            return False

        nmubers.sort()
        joker = 0

        for i in range(len(nmubers)-1):
            if nmubers[i] == 0:
                joker += 1
            elif 0 < nmubers[i+1] - nmubers[i] <= joker + 1:
                joker -= (nmubers[i+1] - nmubers[i] - 1)
            else:
                return False

        return True


s = Solution()
print(s.is_continuous([2, 5, 6, 3, 0]))
print(s.is_continuous([2, 5, 6, 1, 0]))
print(s.is_continuous([2, 5, 4, 1, 3]))
