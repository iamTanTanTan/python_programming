'''
输入两个整数序列， 第一个序列表示栈的压入顺序， 请判断第二个序列是否为该栈的弹出顺序。
假设压入栈的所有数字均不相等。 例如序列1、 2、 3、 4、 5是某栈的压栈序列，
序列4、 5、 3、 2、 1是该压栈序列对应的一个弹出序列， 但4、 3、 5、 1、 2
就不可能是该压栈序列的弹出序列。
'''
'''
入栈序列1,2,3,4,5
出栈序列4,5,3,2,1
首先1入栈辅助stack，此时栈顶1≠4，继续入栈2
此时栈顶2≠4，继续入栈3
此时栈顶3≠4，继续入栈4
此时栈顶4＝4，出栈4，弹出序列向后一位，此时为5，,辅助栈stack里面是1,2,3
此时栈顶3≠5，继续入栈5
此时栈顶5=5，出栈5,弹出序列向后一位，此时为3，,栈popV里面是1,2,3
...
依次执行，最后辅助栈为空。如果不为空说明弹出序列不是该栈的弹出顺序。
'''

class Solution:
    def isPopOrder(self, pushV, popV):
            if pushV == [] or popV == []:
                return False
            stack = []
            # pushV 为入栈序列，popV为出栈序列
            for i in pushV: 
                stack.append(i)
                 # 如果stack不为空且栈顶元素等于popV首元素，弹出stack栈顶元素，弹出序列popV首元素
                while len(stack) and stack[-1] == popV[0]: 
                    # 注意：pop默认从列表中删除并返回“最后一个元素”
                    stack.pop()
                    popV.pop(0)
            # 如果循环结束后辅助栈不为空，返回false，否则返回true
            if len(stack):
                return False
            else:
                return True

pushV = [1, 2, 3, 4, 5]
popV = [4, 5, 3, 2, 1]
popVF = [4, 5, 2, 1, 3]
S = Solution()
print(S.isPopOrder(pushV, popV))
print(S.isPopOrder(pushV, popVF))