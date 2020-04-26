# coding: utf-8

'''
输入两棵二叉树A，B，判断B是不是A的子结构。（ps：我们约定空树不是任意一个树的子结构）
'''
'''
要查找树A中是否存在和树B结构一样的子树， 我们可以分成两步： 第一步在树A中找到和B的根结点的值一样的结点R， 第二步再判断树A
中以R为根结点的子树是不是包含和树B一样的结构。

我们递归调用HasSubtree遍历二叉树A。 如果发现某一结点的值和树B的头结点的值相同， 则调用DoesTree1HaveTree2， 做第二步判断。
第二步是判断树A中以R为根结点的子树是不是和树B具有相同的结构。 同样， 我们也可以用递归的思路来考虑： 如果结点R的值和树B的根
结点不相同， 则以R为根结点的子树和树B肯定不具有相同的结点； 如果它们的值相同， 则递归地判断它们各自的左右结点的值是不是相同。
递归的终止条件是我们到达了树A或者树B的叶结点。
'''

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        
class Solution:
    def HasSubtree(self, pRoot1, pRoot2):
        result = False
        if pRoot1 != None and pRoot2 != None:
            if pRoot1.val == pRoot2.val:
                result = self.DoesTree1haveTree2(pRoot1, pRoot2)                
            if not result:
                result = self.DoesTree1haveTree2(pRoot1.left, pRoot2)
            if not result:
                result = self.DoesTree1haveTree2(pRoot1.right, pRoot2)
        return result
    
    def DoesTree1haveTree2(self, pRoot1, pRoot2):
        if pRoot2 == None: # 如果Tree2已经遍历完了都能对应的上，返回true
            return True
        if pRoot1 == None: #如果Tree2还没有遍历完，Tree1却遍历完了。返回false
            return False
        if pRoot1.val != pRoot2.val: # 如果根节点的值不相等，返回false
            return False
        
        #如果根节点对应的上，那么就分别去子节点里面匹配
        return self.DoesTree1haveTree2(pRoot1.left, pRoot2.left) and self.DoesTree1haveTree2(pRoot1.right, pRoot2.right)
         
                
pRoot1 = TreeNode(8)
pRoot2 = TreeNode(8)
pRoot3 = TreeNode(7)
pRoot4 = TreeNode(9)
pRoot5 = TreeNode(2)
pRoot6 = TreeNode(4)
pRoot7 = TreeNode(7)
pRoot1.left = pRoot2
pRoot1.right = pRoot3
pRoot2.left = pRoot4
pRoot2.right = pRoot5
pRoot5.left = pRoot6
pRoot5.right = pRoot7

pRoot8 = TreeNode(8)
pRoot9 = TreeNode(9)
pRoot10 = TreeNode(2)
pRoot8.left = pRoot9
pRoot8.right = pRoot10

S = Solution()
print(S.HasSubtree(pRoot1, pRoot8))