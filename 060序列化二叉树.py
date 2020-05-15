'''
题目：请实现两个函数，分别用来序列化和反序列化二叉树
'''
'''
思路：
序列化二叉树：把一棵二叉树按照某种遍历方式的结果以某种格式保存为字符串。
    需要注意的是，序列化二叉树的过程中，如果遇到空节点，需要以某种符号（这里用#）表示。
    序列化可以基于先序/中序/后序/按层等遍历方式进行，这里采用先序遍历的方式实现，字符串之间用 “，”隔开。
反序列化二叉树：根据某种遍历顺序得到的序列化字符串，重构二叉树。具体思路是按前序遍历“根左右”的顺序，
    根节点位于其左右子节点的前面，即非空（#）的第一个节点是某子树的根节点，左右子节点在该根节点后，
    以空节点#为分隔符。
'''



class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # 序列化
    def serialize(self, root):
        if not root:
            return '#'

        return str(root.val) +',' + self.serialize(root.left) +',' + self.serialize(root.right)

    # 反序列化
    def deserialize(self, s):
        list1 = s.split(',')
        return self.deserialize_tree(list1)

    def deserialize_tree(self, list1):
        if len(list1) <= 0:
            return None

        val = list1.pop(0)
        root = None

        if val != '#':
            root = TreeNode(int(val))
            root.left = self.deserialize_tree(list1)
            root.right = self.deserialize_tree(list1)

        return root

    # 按层次遍历打印反序列化后的树
    # def printFromTopToBottom(self, root):
    #     queue = []
    #     if not root:
    #         return []

    #     res = []
    #     queue.append(root)
    #     while len(queue) > 0:
    #         current = queue.pop(0)
    #         res.append(current.val)
    #         if current.left:
    #             queue.append(current.left)
    #         if current.right:
    #             queue.append(current.right)
    #     return res

node1 = TreeNode(8)
node2 = TreeNode(6)
node3 = TreeNode(10)
node4 = TreeNode(5)
node5 = TreeNode(7)
node6 = TreeNode(9)
node7 = TreeNode(11)

node1.left = node2
node1.right = node3
node2.left = node4
node2.right = node5
node3.left = node6
node3.right = node7

s = Solution()
print(s.serialize(node1))
print(s.deserialize('8,6,5,#,#,7,#,#,10,9,#,#,11,#,#').val)
# new_tree = s.deserialize('8,6,5,#,#,7,#,#,10,9,#,#,11,#,#')
# print(s.printFromTopToBottom(new_tree))