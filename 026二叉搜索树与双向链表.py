'''
输入一棵二叉搜索树，将该二叉搜索树转换成一个排序的双向链表。
要求不能创建任何新的结点，只能调整树中结点指针的指向。
'''


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# 解体思路：递归实现中序遍历二叉搜索树
# 递归处理左子树，链接根节点与左子树最右节点；
# 递归处理右子树，链接根节点与右子树最左节点
# 向前遍历到第一个节点，返回节点地址


class Solution:
    def convert(self, root):
        if not root:
            return None

        if not root.left and not root.right:
            return root

        # 递归处理左子树
        self.convert(root.left)
        left = root.left

        # 将根节点左指针指向左子树最右孩子，左子树最右孩子的右指针指向根节点
        if left:
            while left.right:
                left = left.right
            root.left, left.right = left, root

        # 递归处理右子树
        self.convert(root.right)
        right = root.right

        # 将根节点右指针指向右子树最左孩子，右子树最左孩子的左指针指向根节点
        if right:
            while right.left:
                right = right.left
            root.right, right.left = right, root

        while root.left:
            root = root.left

        return root


node1 = TreeNode(10)
node2 = TreeNode(6)
node3 = TreeNode(14)
node4 = TreeNode(4)
node5 = TreeNode(8)
node6 = TreeNode(12)
node7 = TreeNode(16)

node1.left = node2
node1.right = node3
node2.left = node4
node2.right = node5
node3.left = node6
node3.right = node7

S = Solution()
new_list = S.convert(node1)
print(new_list.val)
