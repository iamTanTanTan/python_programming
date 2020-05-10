'''
一个链表中包含环，请找出该链表的环的入口结点。
'''


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def loop_entry_node(self, head):
        if not head:
            return None
        # 遍历链表，环的存在，遍历遇见的第一个重复的即为入口节点
        temp = []
        while head:
            if head in temp:
                return head.val
            else:
                temp.append(head)
                head = head.next


node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)
node5 = ListNode(5)
node6 = ListNode(6)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node6
node6.next = node3

s = Solution()
print(s.loop_entry_node(node1))
