# coding: utf-8


'''
定义一个函数，输入一个链表的头结点，反转该链表并输出反转后链表的头结点。
'''

'''
思路一：使用指针思想
1. pre始终指向已反序的最后一个节点
2. middle始终指向当前考察节点
3. after始终指向待反序的第一个节点，也就是middle之后

思路二：python 列表
'''

class ListNode:
    def __init__(self, x=None):
        self.val = x
        self.next = None
        
class Solution: 
    # 指针思想
    def reverseList(self, middle):
        if not middle or not middle.next:
            return middle
        pre = None
        while middle:
            after = middle.next # 把当前节点的下一个节点保存下来
            middle.next = pre # 对考察的结点进行反序
            pre = middle # 更新pre
            middle = after # 后移middle, 换下一个待考察结点
        return pre # 因为pre始终指向已反序的最后一个结点
        
    # python 列表
    def printListFromTailToHead(self, listNode):
        if not listNode:
            return []
        
        result = []
        while listNode:
            result.extend([listNode.val])
            listNode = listNode.next
                
        return result[::-1]
    
node1 = ListNode(10)
node2 = ListNode(11)
node3 = ListNode(13)
node1.next = node2
node2.next = node3

test = Solution()
# print(test.reverseList(node1).val)
print(test.printListFromTailToHead(node1)[0])
