'''
从上往下打印出二叉树的每个节点，同层节点从左至右打印
'''
'''
广度优先层次遍历，利用一个队列来实现
层序遍历的基本过程是：
先根节点入队，然后：
1.从队列中取出一个元素
2.访问该元素所指的结点
3.若该元素所指结点的左、右孩子结点非空，则将其左、右孩子顺序入队
'''
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # 返回从上到下每个节点值列表，例：[1,2,3]
    def printFromTopToBottom(self, root):
        queue = []
        if not root:
            return []

        result = []
        queue.append(root)
        while len(queue) > 0:
            currentRoot = queue.pop(0)
            result.append(currentRoot.val)
            if currentRoot.left:
                queue.append(currentRoot.left)
            if currentRoot.right:
                queue.append(currentRoot.right)
        return result

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
print(S.printFromTopToBottom(node1))

