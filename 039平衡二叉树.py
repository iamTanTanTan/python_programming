'''
输入一棵二叉树，判断该二叉树是否是平衡二叉树。
'''

'''
基于二叉树的深度，再次进行递归。
以此判断左子树的高度和右子树的高度差是否大于1，若是则不平衡，反之平衡。
'''


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def get_depth(self, root):
        if not root:
            return 0

        return max(self.get_depth(root.left), self.get_depth(root.right)) + 1

    def is_balanced(self, root):
        if not root:
            # 返回True是因为这是最后的判断依据，在不断递归中，最后是叶子节点，即终止
            # 如果叶子节点时，依然左右子树之差小于1，那么就是平衡二叉树，返回True
            return True

        if abs(self.get_depth(root.left) - self.get_depth(root.right)) > 1:
            return False

        return self.is_balanced(root.left) and self.is_balanced(root.right)


node1 = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(3)
node4 = TreeNode(4)
node5 = TreeNode(5)
node6 = TreeNode(6)
node7 = TreeNode(7)

node1.left = node2
node1.right = node3
node2.left = node4
node2.right = node5
node3.right = node6
node5.left = node7

S = Solution()
print(S.is_balanced(node1))
