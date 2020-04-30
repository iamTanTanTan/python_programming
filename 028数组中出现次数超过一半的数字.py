'''
数组中有一个数字出现的次数超过数组长度的一半，请找出这个数字。例如输入一个长度为9的数组{1,2,3,2,2,2,5,4,2}。
由于数字2在数组中出现了5次，超过数组长度的一半，因此输出2。如果不存在则输出0。
'''
'''
根据数组的特点，出现次数超过一半的数(众数)，他出现的次数比其他数字出现的总和还要多，如果众数存在，
则每次从数组中剪除和众数相同个数的元素，剩余数组的众数不变。因此可以设计一个计数器，初值为1，
从第二个数起依次和“第一个”数比较，若相等则计数器加一，否则减一。当计数器变为零时，剪除前面部分。
众数候选者改为新的当前元素，计数器重新更新为一，如此迭代直到最后。若最终计数器不为零，则众数存在，否则不存在。
'''


class Solution:
    def majority_candidate(self, numbers):
        if not numbers:
            return 0

        # 初始众数候选设为首元素
        maj = numbers[0]
        # 初始计数器
        count = 1
        for i in range(1, len(numbers)):
            # 每当计数器归零,都意味着此时的前缀可以剪除
            if count == 0:
                # 众数候选者改为新的当前元素
                maj = numbers[i]
                # 计数器重置为1
                count = 1

            elif numbers[i] == maj:
                # 相应的更新差额计数器
                count += 1

            else:
                count -= 1
        # 若计数器为零，则不存在众数，返回0
        if not count:
            return 0

        # 至此，若原众数存在，则只能是maj，尽管反之不亦然
        return maj


S = Solution()
print(S.majority_candidate([1, 2, 3, 2, 2, 2, 5, 4, 2]))
print(S.majority_candidate([1, 2, 3, 3, 3, 3, 4]))
print(S.majority_candidate([1, 2]))
print(S.majority_candidate([]))

