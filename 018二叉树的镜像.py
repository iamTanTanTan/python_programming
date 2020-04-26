# coding: utf-8


'''
请完成一个函数， 输入一个二叉树， 该函数输出它的镜像.
'''
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        
class Solution:
    def mirror(self, root):
        if root == None:
            return
        if root.left == None and root.right == None:
            return root
        
        root.left, root.right = root.right, root.left #交换根节点的左右子树root.left和root.right
        
        self.mirror(root.left) #交换root.left的子树
        self.mirror(root.right) #交换root.right的子树
                
pNode1 = TreeNode(8)
pNode2 = TreeNode(6)
pNode3 = TreeNode(10)
pNode4 = TreeNode(5)
pNode5 = TreeNode(7)
pNode6 = TreeNode(9)
pNode7 = TreeNode(11)

pNode1.left = pNode2
pNode1.right = pNode3
pNode2.left = pNode4
pNode2.right = pNode5
pNode3.left = pNode6
pNode3.right = pNode7

S = Solution()
S.mirror(pNode1)
print(pNode1.right.left.val)
        