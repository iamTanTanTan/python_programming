'''
输入一颗二叉树和一个整数，打印出二叉树中结点值的和为输入整数的所有路径。
路径定义为从树的根结点开始往下一直到叶结点所经过的结点形成一条路径。
'''

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # 返回二维列表，内部每个列表表示找到的路径
    def findPath(self, root, sum):
        if not root:
            return None
        if root.left == None and root.right == None:
            if sum == root.val:
                # 注意这里如果写成一维列表，则返回的是符合要求的路径值的和而非路径值
                return [[root.val]]
            else:
                # 注意这里不要return None,否则找到符合要求的路径后无法返回
                return []
        # 对左右子树所有结点依次判断
        a = self.findPath(root.left, sum-root.val) + self.findPath(root.right, sum-root.val)
        # 找到符合要求的叶结点后按照相反路径将其根结点依次插在前面
        return [[root.val] + i for i in a]


node1 = TreeNode(10)
node2 = TreeNode(5)
node3 = TreeNode(12)
node4 = TreeNode(4)
node5 = TreeNode(7)


node1.left = node2
node1.right = node3
node2.left = node4
node2.right = node5


S = Solution()
print(S.findPath(node1, 22))
