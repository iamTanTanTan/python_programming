# coding: utf-8

'''
输入某二叉树的前序遍历和中序遍历的结果，请重建出该二叉树。
假设输入的前序遍历和中序遍历的结果中都不含重复的数字。
例如输入前序遍历序列[1,2,4,7,3,5,6,8]和中序遍历序列[4,7,2,1,5,3,8,6]，则重建二叉树并返回。
'''


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        
class Solution:
    # 返回构造的TreeNode结点
    def reConstructBinaryTree(self, pre_order, mid_order):
        if not pre_order or not mid_order:
            return None
        if set(pre_order) != set(mid_order):
            return None
        
        root = TreeNode(pre_order[0])
        i_root = mid_order.index(pre_order[0])
        root.left = self.reConstructBinaryTree(pre_order[1:i_root+1], mid_order[:i_root])  
        root.right = self.reConstructBinaryTree(pre_order[i_root+1:], mid_order[i_root+1:])
        return root
          
    
pre_order = [1, 2, 3, 5, 6, 4]
mid_order = [5, 3, 6, 2, 4, 1]
test = Solution()
newTree = test.reConstructBinaryTree(pre_order, mid_order)

# 按层序遍历输出树中某一层的值
def printNodeAtLevel(treeNode, level):
    if not treeNode or level < 0:
        return 0
    if level == 0:
        print(treeNode.val)
        return 1
    printNodeAtLevel(treeNode.left, level-1)
    printNodeAtLevel(treeNode.right, level-1)
    
# 已知树的深度按层遍历输出树的值
def printNodeByLevel(treeNode, depth):
    for level in range(depth):
        printNodeAtLevel(treeNode, level)
# 验证结果   
printNodeAtLevel(newTree, 3)
printNodeByLevel(newTree, 4)
