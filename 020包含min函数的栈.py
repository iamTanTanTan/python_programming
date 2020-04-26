'''
我们可以设计两个栈：stack和minStack，stack就是普通的栈，minStack用来存储push进来的最小值。
首先是push操作：
第一个元素同时压入两个栈中，此后每次压入的数据newNum都push进Stack中，
然后比较newNum与minStack栈顶元素的大小，如果newNum较小，则同步将newNum压入minStack中,
如果newNum较大，就把最小值压入minStack中。
弹出时，同步弹出，这是一个栈结构。
注意：两个栈中的元素个数始终相同。
'''

class Solution:
    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, node):
        self.stack.append(node)
        if self.minStack == [] or node < self.min():
            self.minStack.append(node)
        else:
            temp = self.min()
            self.minStack.append(temp)

    def pop(self):
        if self.stack == [] or self.minStack == []:
            return None
        self.minStack.pop()
        self.stack

    def top(self):
        return self.stack[-1]

    def min(self):
        return self.minStack[-1]

S = Solution()
S.push(3)
S.push(4)
S.push(2)
S.push(1)
print(S.min())
S.pop()
print(S.min())
S.pop()
print(S.min())
