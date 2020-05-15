'''
给定一颗二叉搜索树，请找出其中的第k小的结点。例如，
    5
   / \
  3  7
 /\ /\
2 4 6 8 中，
按结点数值大小顺序第三个结点的值为4。
'''

'''
思路：二叉搜索树按照中序遍历的顺序打印出来正好就是排序好的顺序。
     所以，中序遍历第k个数就是结果。
'''


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


result = []


class Solution:

    # 方法一

     def kth_node1(self, root, k):
        if not root:
            return None

        stack = []
        while root or stack:
            while root:
                # 将根节点和左子树左节点依次入栈
                stack.append(root)
                root = root.left
            root = stack.pop()
            k -= 1
            if k == 0:
                return root
            root = root.right

    # 方法二

    def kth_node2(self, pRoot, k):
        global result
        middle = self.mid_order(pRoot)
        if k <= 0 or len(middle) < k:
            return None
        else:
            return result[k-1]

     # 中序遍历
    def mid_order(self, root):
        if not root:
            return []

        self.mid_order(root.left)
        result.append(root)
        self.mid_order(root.right)

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

s = Solution()
# 注意题目要求是返回结点还是结点的值
print(s.kth_node1(node1, 3))
print(s.kth_node1(node1, 3).val)
print(s.kth_node2(node1, 3))
print(s.kth_node2(node1, 3).val)
