'''
题目：如何得到一个数据流中的中位数？
如果从数据流中读出奇数个数值，那么中位数就是所有数值排序之后位于中间的数值。
如果从数据流中读出偶数个数值，那么中位数就是所有数值排序之后中间两个数的平均值。
'''

'''
思路：

采用优先队列，也就是大根堆跟小根堆，我们将较小的n/2个数放到大根堆中，将较大的n/2个数放到小根堆中
1. 如果n是偶数,那么大根堆的堆顶跟小根堆的堆顶就是我们要找的两个中位数，将其相加除以2作为结果返回即可。
2. 如果n是奇数，那么就看大根堆跟小根堆谁的节点个数比另一个堆多一个，
    节点数量多的那个堆的堆顶就是我们要找的中位数，此时我们直接返回结果即可。


需要注意的是:

1.对于取堆顶元素的操作的时间复杂度是常数级别的。

2.插入新节点时我们需要判断节点的值是否小于大根堆堆顶的值或者大于小根堆堆顶的值，
  如果小于大根堆堆顶的值，那么节点应该插入大根堆，反过来应该插入小根堆。

3.每次插入新节点我们还需要判断两个堆之间的元素个数是否平衡。插入新节点后，我们判断两个堆的元素个数，
  如果相差为2那么我们就要对堆进行调整。比如新插入一个节点到小根堆中，
  而此时大根堆的个数+1小于小根堆的节点个数，这个时候只需要将小根堆的堆顶元素弹出，
  然后将这个弹出的元素插入大根堆即可。反过来也是一样的操作。为什么可以这样做呢？
  这是因为我们说了小根堆保存的是较大的n/2个数，而小根堆的堆顶是小根堆中最小的元素，
  同时也是大根堆中最大的元素，因此我们将这个堆顶元素弹出并插入大根堆的操作并不会破坏
  “小根堆保存较大的n/2个数，大根堆保存较小的n/2”这样的前提。
'''

import heapq

class Solution:
    def __init__(self):
        self.max_heap = []
        self.min_heap = []

    def insert(self, num):
        if not self.max_heap:
            # python的heaqp模块是小根堆，因此要保存大根堆的话需要加上一个负号
            heapq.heappush(self.max_heap, -num)
            # 此处return不要忘记，否则不能连续插入数据流
            return

        if num > -self.max_heap[0]:
            heapq.heappush(self.min_heap, num)
            if len(self.max_heap) + 1 < len(self.min_heap):
                # 将min_heap堆顶元素依次转移到max_heap
                # 插入大根堆需要给值加负号
                heapq.heappush(self.max_heap, -heapq.heappop(self.min_heap))
        else:
            heapq.heappush(self.max_heap, -num)
            if len(self.min_heap) + 1 < len(self.max_heap):
                # 弹出大根堆堆顶的时候需要加负号变为正数
                heapq.heappush(self.min_heap, -heapq.heappop(self.max_heap))

    def get_median(self):
        # 大根堆元素多一个，中位数是大根堆堆顶
        if len(self.min_heap) < len(self.max_heap):   
            return -self.max_heap[0]
        # 小根堆元素多一个，中位数是小根堆堆顶
        if len(self.max_heap) < len(self.min_heap):  
            return self.min_heap[0]
        else:
            # 大小跟堆元素一样多，则中位数是两者堆顶之和除以2
            return (-self.max_heap[0] + self.min_heap[0])/2 

if __name__ == '__main__':
    s = Solution()
    s.insert(1)
    result = s.get_median()
    print(result)

    s.insert(2)
    result=s.get_median()
    print(result)

    s.insert(3)
    result=s.get_median()
    print(result)

    s.insert(4)
    result=s.get_median()
    print(result)