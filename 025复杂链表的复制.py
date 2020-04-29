'''
题目：输入一个复杂链表（每个节点中有节点值，以及两个指针，一个指向下一个节点，
另一个特殊指针指向任意一个节点），返回结果为复制后复杂链表的head。
注意，输出结果中请不要返回参数中的节点引用，否则判题程序会直接返回空）
'''

'''
思路一：
使用python标准库copy的deepcopy

思路二：
将大问题转变为小问题，每次都进行复制头部节点，然后进行递归，每次同样处理头部节点。

思路三：
1. 复制原始链表的任意结点N并创建新结点N'， 再把N'链接到N的后面。
2. 第二步设置复制出来的结点的随机指针random，如果原始链表上的结点N的随机指针random指向S， 
   则它对应的复制结点N'的随机指针random指向S的下一结点S'。
3. 把这个长链表拆分成两个链表： 把奇数位置的结点用next链接起来
   就是原始链表， 把偶数位置的结点用next链接起来就是复制出来的链表。 
'''


import copy
class RandomListNode:
    def __init__(self, x):
        self.label = x
        # next为链表普通指针
        self.next = None
        # random为链表随机指针
        self.random = None

# 方法一
class Solution1:
    # 返回 RandomListNode
    def clone(self, head):
        new_head = copy.deepcopy(head)
        return new_head.label

#方法二
class Solution2:
    # 返回RandomListNode
    def clone(self, head):
        # 复制头部节点
        if head is None:
            return None

        new_head = RandomListNode(head.label)
        new_head.next = head.next
        new_head.random = head.random

        # 递归其他节点
        new_head.next = self.clone(head.next)

        return new_head.label

node1 = RandomListNode(1)
node2 = RandomListNode(3)
node3 = RandomListNode(5)
node1.next = node2
node2.next = node3
node1.random = node3

S1 = Solution1()
S2 = Solution2()
print(S1.clone(node1))
print(S2.clone(node1))


# 
class Solution3:
    # 返回 RandomListNode
    def clone(self, head):
        if head == None:
            return None
        self.clone_nodes(head)
        self.connect_random_nodes(head)
        return self.reconnect_nodes(head)

    # 复制原始链表的每个结点, 将复制的结点链接在其原始结点的后面
    def clone_nodes(self, head):
        node = head
        while node:
            cloned = RandomListNode(0)
            cloned.label = node.label
            cloned.next = node.next

            node.next = cloned
            node = cloned.next

    # 将复制后的链表中的复制结点的random指针链接到被复制结点random指针的后一个结点
    def connect_random_nodes(self, head):
        node = head
        while node:
            cloned = node.next
            if node.random != None:
                cloned.random = node.random.next
            node = cloned.next

    # 拆分链表, 将原始链表的结点组成新的链表, 复制结点组成复制后的链表
    def reconnect_nodes(self, head):
        node = head
        cloned_head = new_head = node.next
        node.next = cloned_head.next
        node = node.next

        while node:
            new_head.next = node.next
            new_head = new_head.next
            node.next = new_head.next
            node = node.next

        return cloned_head


# node1 = RandomListNode(1)
# node2 = RandomListNode(3)
# node3 = RandomListNode(5)
# node1.next = node2
# node2.next = node3
# node1.random = node3

# S3 = Solution3()
# print(S.clone(node1).label)
