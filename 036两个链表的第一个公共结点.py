'''
输入两个单向链表，找出它们的第一个公共结点
'''
'''
如果两个单向链表有公共的结点， 那么这两个链表从某一结点开始， 它们的m_pNext都指向同一个
结点。 但由于是单向链表的结点， 每个结点只有一个m_pNext， 因此从第一个公共
结点开始， 之后它们所有结点都是重合的， 不可能再出现分叉。 

分析：先依次遍历两个链表，记录两个链表的长度m和n，如果 m > n，那么我们就先让长度为m的链表走m-n个结点，
然后两个链表同时遍历，当遍历到相同的结点的时候停止即可。对于 m < n，同理。
'''


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def first_common_node(self, head1, head2):
        # 获取两个链表的长度差
        len1 = self.get_length(head1)
        len2 = self.get_length(head2)
        len_diff = abs(len1 - len2)

        if len1 < len2:
            short = head1
            long = head2

        else:
            short = head2
            long = head1

        # 长链表先走多出的结点数
        for i in range(len_diff):
            long = long.next

        # 两个链表同时遍历,直到为空或者找到第一个公共结点结束
        while short != None and long != None and short != long:
            short = short.next
            long = long.next

        # return long结果一样
        return short

    # 获取链表长度
    def get_length(self, head):
        len = 0
        while head:
            head = head.next
            len += 1
        return len


test = Solution()
node1 = ListNode(10)
node2 = ListNode(11)
node3 = ListNode(13)
node4 = ListNode(14)
node1.next = node2
node2.next = node3
node3.next = node4

node5 = ListNode(7)
node6 = ListNode(13)
node5.next = node6
node6.next = node4

print(test.first_common_node(node1, node5).val)
