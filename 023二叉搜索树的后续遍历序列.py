'''
输入一个整数数组， 判断该数组是不是某二叉搜索树的后序遍历的结果。
如果是则返回true， 否则返回false。 假设输入的数组的任意两个数字都互不相同。
'''

'''
二叉搜索树即是二叉排序树，
1. 后序遍历序列的最后一个元素为二叉树的根节点；
2. 二叉搜索树左子树上所有的结点均小于根结点、右子树所有的结点均大于根结点。
算法步骤如下：
1. 找到根结点；
2. 遍历序列，找到第一个大于等于根结点的元素i，则i左侧为左子树、i右侧为右子树；
3. 我们已经知道i左侧所有元素均小于根结点，那么再依次遍历右侧，看是否所有元素均大于根结点；若出现小于根结点的元素，则直接返回false；若右侧全都大于根结点，则：
4. 分别递归判断左/右子序列是否为后序序列；
'''

class Solution:
    def verifySequenceOfBST(self, sequence):
        if sequence == []:
            return False

        root = sequence[-1]
        length = len(sequence)
        if root < min(sequence) or max(sequence) < root:
            return True
        index = 0

        '''
        下面这个for循环特别需要主要index=i必须写在if语句外面,
        否则就会发生当root结点前的所有元素小于root的时候, 正确判断应该为True,
        但是因为if语句没有进入, index = 0 ,
        在进入二叉搜索树的右子树结点大于根结点的for循环的时候, 因为sequence的数都小于root, 就会判断出错
        '''
        for i in range(length-1): 
            index = i
            if sequence[i] > root:
                break

        # 注意这个循环起始点必须是index+1, sequence[index]前面已判断出大于root
        for j in range(index+1, length-1):
            if sequence[j] < root:
                return False
        # 判断左子树
        left = True
        if index > 0:
            left = self.verifySequenceOfBST(sequence[:index])

        # 判断右子树
        right = True
        if index < length - 1:
            # 注意这里起点为index,根节点在最后，左右子树序列是连续的
            right = self.verifySequenceOfBST(sequence[index:length-1])
        return left and right

array1 = [5, 7, 6, 9, 11, 10, 8]
array2 = [4, 6, 7, 5]
array3 = [1, 2, 3, 4, 5]
S = Solution()
print(S.verifySequenceOfBST(array1))
print(S.verifySequenceOfBST(array2))
print(S.verifySequenceOfBST(array3))


