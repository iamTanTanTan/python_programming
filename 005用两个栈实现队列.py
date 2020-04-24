# coding: utf-8

'''用两个栈来实现一个队列，完成队列的Push和Pop操作, 队列中的元素为int类型'''

'''
思路：需要两个栈Stack1和Stack2，push的时候直接push进Stack1。
pop需要判断Stack1和Stack2中元素的情况，Stack1空的话，
直接从Stack2 pop，Stack1不空的话，把Stack1的元素push进入Stack2,
然后pop Stack2的值。
'''

class Solution:
    def __init__(self):
        self.stackA = []
        self.stackB = []

    def push(self, node):
        self.stackA.append(node)

    def pop(self):
        if len(self.stackA) == 0 and len(self.stackB) == 0:
            return
        elif len(self.stackB) == 0:
            while len(self.stackA) > 0:
                self.stackB.append(self.stackA.pop())
        return self.stackB.pop()

P = Solution()
P.push(1)
P.push(2)
P.push(3)
print(P.pop())
P.push(4)
print(P.pop())
print(P.pop())
print(P.pop())
print(P.pop())