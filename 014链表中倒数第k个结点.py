# coding: utf-8


'''
输入一个链表，输出该链表中倒数第k个结点。
'''

'''
使用列表的切片
'''
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
        
        
class Solution:
    def FindKthToTail(self, head, k):
        # write code here
        res = []
        while head:
            res.append(head)
            head = head.next
        if len(res) < k or k < 1:
            return
        return res[-k]        
    

test = Solution()
node1 = ListNode(10)
node2 = ListNode(11)
node3 = ListNode(13)
node4 = ListNode(14)
node1.next = node2
node2.next = node3
node3.next = node4


test = Solution()
print(test.FindKthToTail(node1, 1).val)