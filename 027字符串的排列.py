'''
输入一个字符串,按字典序打印出该字符串中字符的所有排列。
例如输入字符串abc,则打印出由字符a,b,c所能排列出来的所有字符串abc,acb,bac,bca,cab和cba。
'''

'''
思路一：
使用python标准库itertools中permutations函数输入参数为一个可迭代对象，返回一个迭代器，
然后使用join函数将返回的字符“串”起来

思路二：
化复杂为简单，如何找到解这道题的通式呢？和青蛙跳台阶的思路一样，
无论给定的字符串长度多少，其排列出来的组合样式均可以分解为“第一个字符+剩下的字符”的样式。
可以通过遍历分别赋予第一位上不同的字符，那“剩下的字符”又可以如上分解。
'''


# 方法一




import itertools
class Solution1:
    def permutation(self, ss):
        res = set(itertools.permutations(ss))
        return sorted(list(map(lambda x: ''.join(x), res)))

# 因为map函数返回的是一个序列，所以需要调用for循环来获取序列中每一个元素。
# 如果给定的字符串不包含重复元素，或者虽然包含重复元素，
# 将重复的每个元素看做互不相同的独立的元素的话,代码如下

# 方法二


class Solution2:
    def permutation(self, ss):
        res = []
        if len(ss) <= 1:
            return ss

        for i in range(len(ss)):
            # map() 会根据提供的函数对指定序列做映射。
            for j in map(lambda x: ss[i] + x, self.permutation(ss[:i] + ss[i+1:])):
                res.append(j)
                res.sort()

        return res

# 当需要考虑重复元素时，加一个判断即可。


class Solution3:
    def permutation(self, ss):
        res = []
        if len(ss) <= 1:
            return ss

        for i in range(len(ss)):
            # map() 会根据提供的函数对指定序列做映射。
            for j in map(lambda x: ss[i] + x, self.permutation(ss[:i] + ss[i+1:])):
                if j not in res:
                    res.append(j)
                    res.sort()

        return res


ss = 'aacb'
S1 = Solution1()
S2 = Solution2()
S3 = Solution3()
print(S1.permutation(ss))
print(S2.permutation(ss))
print(S3.permutation(ss))
