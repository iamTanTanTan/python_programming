'''
题目：请实现一个函数按照之字形打印二叉树，即第一行按照从左到右的顺序打印，
第二层按照从右至左的顺序打印，第三行按照从左到右的顺序打印，其他行以此类推。
'''

'''
层序打印即可, 分奇偶。
'''


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # 返回从上到下每个节点值列表，例：[1,2,3]
    def z_print(self, root):
        queue = []
        if not root:
            return []

        i = -1
        res = []
        queue.append(root)
        while len(queue) > 0:
            i += 1
            temp = []
            for _ in range(len(queue)):
                current = queue.pop(0)
                temp.append(current.val)
                if current.left:
                    queue.append(current.left)
                if current.right:
                    queue.append(current.right)
            # i从0开始，若i为奇数，反转temp
            if i % 2:
                temp.reverse()
            res.extend(temp)
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
print(S.z_print(node1))
