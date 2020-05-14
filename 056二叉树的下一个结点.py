'''
题目：给定一个二叉树和其中的一个结点，请找出中序遍历顺序的下一个结点并且返回。注意，树中的结点不仅包含左右
子结点，同时包含指向父结点的指针。
'''

'''
思路：
（1） 若该节点存在右子树：则下一个节点为右子树最左子节点
（2） 若该节点不存在右子树：这时分两种情况：
 2.1 该节点为父节点的左子节点，则下一个节点为其父节点
 2.2 该节点为父节点的右子节点，则沿着父节点一直向上查找到B（B为其父节点的左子节点），
     则B的父节点A为下一个节点
     2.2 包括了2.1的情形
 
'''


class TreeLinkNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None


class Solution:
    def get_next(self, node):
        if node == None:
            return None

        # 1. 寻找右子树，如果存在就一直找，直到右子树的最左边就是下一个节点
        if node.right:
            node = node.right
            while node.left:
                node = node.left
            return node
        # 2.没有右子树，则沿着父节点一直向上查找到B（B为其父节点的左子节点），
        #   则B的父节点A为下一个节点
        else:
            while node.next:
                if node.next.left == node:
                    return node.next
                # 重新赋值,下次循环中继续找父节点的父节点
                node = node.next

        return None


node1 = TreeLinkNode(7)
node2 = TreeLinkNode(4)
node3 = TreeLinkNode(12)
node4 = TreeLinkNode(2)
node5 = TreeLinkNode(6)
node6 = TreeLinkNode(1)
node1.left = node2
node1.right = node3
node2.left = node4
node2.right = node5
node4.left = node6
node6.next = node4
node4.next = node2
node5.next = node2
node2.next = node1
node3.next = node1
s = Solution()
print(s.get_next(node1).val)
print(s.get_next(node5).val)
print(s.get_next(node6).val)

