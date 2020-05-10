'''
请实现一个函数用来匹配包括’.‘和’*‘的正则表达式。模式中的字符’.‘表示任意一个字符，
而’'表示它前面的字符可以出现任意次（包含0次）。 在本题中，匹配是指字符串的所有字符匹配整个模式。
例如，字符串"aaa"与模式"a.a"和"abaca"匹配，但是与"aa.a"和"aba"均不匹配
'''

'''
思路：本题就是很直观的字符串的匹配，难点在于当遇到模式中两个特殊字符怎么处理和对于各种形式字符串的全面考虑。
这里采用递归的方式，每次只匹配s中一个字符（模式串pattern， 被匹配字符串s）：处理判断过程如下：

如果 s和pattern都为空，匹配成功
如果pattern是空串，而s不是，匹配失败
如果s，pattern均不是空串(长度至少为1)，考虑到pattern中‘ * ’前字符可以出现0次，
所以不能简单比较s和pattern的第一个字符是否相等，这里分为两种情况考虑：

    如果pattern的第二个字符是‘ * ’：
        如果s与pattern的第一个字符匹配（即s与pattern的第一个字符相等或者pattern第一个字符为‘ . ’)，
        剩余部分有三种匹配情形：
        (1).例如s=aaab，pattern=a*b，‘ * ’前的字符在s中出现不止一次，需s后移一位；
        (2).例如s=abb，pattern=a*abb，此时‘ * ’前后字符相同，所以这里实际上s与pattern的第三个字符匹配。
            需pattern后移两位，同时s不变，相当于忽略x*，认为‘ * ’前的字符在s中出现了0次，；
        (3).例如s=abb，pattern=a*bb，‘ * ’前的字符在s中只出现一次，需pattern后移两位，同时s后移一位，
        否则仅模式串pattern后移两位，s不变，含义同上；
        情况(3)可以被情况(1)和情况(2)包含。
    如果pattern的第二个字符不是‘ * ’：
        如果s与pattern的第一个字符匹配（含义同上），
        s和pattern同时后移一位，继续匹配；否则匹配失败
'''


class Solution:
    # s, pattern都是字符串
    def match(self, s, pattern):
        if len(s) == 0 and len(pattern) == 0:
            return True
        if len(s) > 0 and len(pattern) == 0:
            return False

        # 如果模式第二个字符是*
        if len(pattern) > 1 and pattern[1] == '*':
            if len(s) > 0 and (s[0] == pattern[0] or pattern[0] == '.'):
                # 如果第一个字符匹配，剩余部分有三种匹配情形：
                # 1.字符串后移1位；2.模式后移2位 3.字符串后移1位，模式后移2位
                # 情况(3)可以被情况(1)和情况(2)包含
                return self.match(s[1:], pattern) or self.match(s, pattern[2:])
            else:
                # 如果第一个字符不匹配，模式往后移2位，相当于忽略x*
                return self.match(s, pattern[2:])

        # 如果模式第二个字符不是*
        # 如果s与pattern的第一个字符匹配,s和pattern同时后移一位，继续匹配；否则匹配失败
        elif len(s) > 0 and (s[0] == pattern[0] or pattern[0] == '.'):
            return self.match(s[1:], pattern[1:])
        else:
            return False


s = Solution()
print(s.match('abb', 'a*bb'))
print(s.match('aaa', 'ab*ac*a'))
print(s.match('aaa', 'aa.a'))
