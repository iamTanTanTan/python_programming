'''
删除链表中重复的结点
在一个排序的链表中，存在重复的结点，请删除该链表中重复的结点，重复的结点不保留，返回链表头指针。
例如，链表1->2->3->3->4->4->5 处理后为 1->2->5
'''

'''
思路：将链表里面所有的数存在一个列表里面，然后把列表里面只出现一次的数提取出来，再新建一个链表放进去
'''


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def delete_duplication(self, head):
        res = []
        while head:
            res.append(head.val)
            head = head.next

        # filter函数和map相似，但是filter是返回布尔值去去输入列表进行判断
        # filter判断后的res里面都是只出现一次的数
        # 若要去重并保留重复结点，可使用如下方法：
        # l1 = ['b','c','d','b','c','a','a']
        # l2 = sorted(set(l1), key=l1.index)
        res = list(filter(lambda c: res.count(c) == 1, res))

        # 新建一个列表new存放只出现一次的数
        new = ListNode(0)
        pre = new
        for i in res:
            pre.next = ListNode(i)
            pre = pre.next

        return new.next


node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(3)
node5 = ListNode(4)
node6 = ListNode(4)
node7 = ListNode(5)
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node6
node6.next = node7

s = Solution()
print(s.delete_duplication(node1).next.next.val)
