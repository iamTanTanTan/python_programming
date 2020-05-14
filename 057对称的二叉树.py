'''
题目：请实现一个函数，用来判断一棵二叉树是不是对称的。
注意，如果一个二叉树同此二叉树的镜像是同样的，定义其为对称的。
'''


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def is_symmetrical(self, root):
        return self.is_mirror(root, root)

    def is_mirror(self, root1, root2):
        if root1 == None and root2 == None:
            return True

        if root1 == None or root2 == None:
            return False

        if root1.val != root2.val:
            return False

        return self.is_mirror(root1.left, root2.right) and self.is_mirror(root1.right, root2.left)


node1 = TreeNode(8)
node2 = TreeNode(6)
node3 = TreeNode(10)
node4 = TreeNode(5)
node5 = TreeNode(7)
node6 = TreeNode(10)
node7 = TreeNode(10)

node1.left = node2
node1.right = node3
node2.left = node4
node2.right = node5
node3.left = node6
node3.right = node7

S = Solution()
print(S.is_symmetrical(node1))
print(S.is_symmetrical(node3))
