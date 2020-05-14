'''
从上到下按层打印二叉树，同一层结点从左至右输出。每一层输出一行。
'''


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # 返回从上到下每个节点值列表，例：[1,2,3]
    def print2(self, root):
        if not root:
            return []

        queue = []
        res = []
        queue.append(root)
        while queue:
            temp = []
            for _ in range(len(queue)):
                current = queue.pop(0)
                temp.append(current.val)
                if current.left:
                    queue.append(current.left)
                if current.right:
                    queue.append(current.right)
            # 注意这里把append换成extend则将所有层打印到一行
            res.append(temp)

        return res


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

S = Solution()
print(S.print2(node1))
