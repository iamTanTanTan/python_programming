# coding: utf-8

'''
输入两个递增排序的链表，合成这两个链表并使新链表中的结点仍然是递增排序的
'''

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
        
class Solution:
    def merge(self, pHead1, pHead2):
        if pHead1 == None:
            return pHead2
        elif pHead2 == None:
            return pHead1
        
        pMergedHead = None
        if pHead1.val < pHead2.val:
            pMergedHead = pHead1
            pMergedHead.next = self.merge(pHead1.next, pHead2)
        else:
            pMergedHead = pHead2
            pMergedHead.next = self.merge(pHead1, pHead2.next)
        return pMergedHead
    
node1 = ListNode(1)
node2 = ListNode(3)
node3 = ListNode(5)
node1.next = node2
node2.next = node3

node4 = ListNode(2)
node5 = ListNode(4)
node6 = ListNode(6)
node4.next = node5
node5.next = node6

S = Solution()
S.merge(node1, node4)
print(node4.next.val)