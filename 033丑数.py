'''
我们把只包含因子2、 3和5的数称作丑数（ Ugly Number） 。
求按从小到大的顺序的第1500个丑数。 例如6、 8都是丑数， 但14不是，
因为它包含因子7。 习惯上我们把1当做第一个丑数。
'''

'''
思路：所谓一个数m是另一个数n的因子， 是指n能被m整除， 也就是n%m＝ 0。 根据丑数
的定义， 丑数只能被2、 3和5整除。 也就是说如果一个数能被2整除， 我们把它连续
除以2； 如果能被3整除， 就连续除以3； 如果能被5整除， 就除以连续5。 如果最后我
们得到的是1， 那么这个数就是丑数， 否则不是。
'''


class Solution:
    # 获取第index个丑数
    def get_ugly_num(self, index):
        if index < 1:
            return 0
        # Create an index size list, res[0] = 1
        res = [1] * index
        i2, i3, i5 = 0, 0, 0

        for i in range(1, index):
            # res = 2^(a)*3^(b)*5^(c)
            res[i] = min(res[i2]*2, res[i3]*3, res[i5]*5)

            if res[i] == res[i2]*2:
                i2 += 1
            if res[i] == res[i3]*3:
                i3 += 1
            if res[i] == res[i5]*5:
                i5 += 1

        return res[-1]


s = Solution()
print(s.get_ugly_num(1500))
