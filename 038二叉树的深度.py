'''
输入一棵二叉树，求该树的深度。
从根结点到叶结点依次经过的结点（含根、叶结点）形成树的一条路径，最长路径的长度为树的深度。
'''

'''
利用递归实现。如果一棵树只有一个结点，那么它的深度为1。递归的时候无需判断左右子树是否存在，
因为如果该节点为叶节点，它的左右子树不存在，那么在下一级递归的时候，直接return 0。
同时，记得每次递归返回值的时候，深度加一操作。
'''


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def tree_depth(self, root):
        if root == None:
            return 0
        else:
            return max(self.tree_depth(root.left), self.tree_depth(root.right)) + 1


node1 = TreeNode(7)
node2 = TreeNode(4)
node3 = TreeNode(12)
node4 = TreeNode(2)
node5 = TreeNode(6)
node6 = TreeNode(1)
node1.left = node2
node1.right = node3
node2.left = node4
node2.right = node5
node4.left = node6
s = Solution()
print(s.tree_depth(node1))
