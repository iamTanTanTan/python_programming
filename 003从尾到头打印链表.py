# coding: utf-8

'''
输入一个链表，按链表值从尾到头的顺序返回一个ArrayList。
'''

'''
方法一：使用extend，在尾部插入，其实最关键在于[::-1],只不过输入数据多样化，有可能还是集合，所以转成列表
这个方法效率应该还可以，先存入vector，再反转vector
'''

class ListNode:
    def __init__(self, x=None):
        self.val = x
        self.next = None


class Solution:
    # 返回从尾部到头部的列表值序列，例如[1,2,3]
    def printListFromTailToHead(self, listNode):
        if not listNode:
            return []
        
        result = []
        while listNode:
            result.extend([listNode.val])
            listNode = listNode.next
                
        return result[::-1]
    
    
# =============================================================================
#         另一种写法
#         result = []
#         while listNode.next is not None:
#             result.extend([listNode.val])
#             listNode = listNode.next
#         result.extend([listNode.val])
#         
#         return result[::-1]
# =============================================================================
    
node1 = ListNode(10)
node2 = ListNode(11)
node3 = ListNode(13)
node1.next = node2
node2.next = node3

singleNode = ListNode(12)

test = ListNode()

S = Solution()
print(S.printListFromTailToHead(node1))
print(S.printListFromTailToHead(test))
print(S.printListFromTailToHead(singleNode))
    

'''方法二： 使用insert直接在头部插入'''

class ListNode:
    def __init__(self, x=None):
        self.val = x
        self.next = None
        
class Solution:
    # 返回从尾部到头部的列表值序列，例如[1,2,3]
    def printListFromTailToHead(self, listNode):
        if not listNode:
            return []
        
        result = []
        
        
        while listNode:
            result.insert(0, listNode.val)
            listNode = listNode.next
        return result
            

node1 = ListNode(10)
node2 = ListNode(11)
node3 = ListNode(13)
node1.next = node2
node2.next = node3

singleNode = ListNode(12)

test = ListNode()

S = Solution()
print(S.printListFromTailToHead(node1))
print(S.printListFromTailToHead(test))
print(S.printListFromTailToHead(singleNode))
    
        