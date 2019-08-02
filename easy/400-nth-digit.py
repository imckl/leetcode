# Find the nth digit of the infinite integer sequence 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, ...
# https://leetcode-cn.com/problems/nth-digit/


# 规律：1-9有9个数，10-99有20*9个数字，100-999有300*9个数字，1000-9999有4000*9个数字
class Solution(object):

    def findNthDigit(self, nth: int) -> int:
        # 所在位数规律：9 * pow(10, i - 1) * i
        i, max_count = 0, 0
        while max_count < nth:
            i += 1
            max_count += i * (9 * 10 ** (i - 1))

        # 起始值对应的次数(nth)
        start_count = max_count - i * (9 * 10 ** (i - 1))

        power = i - 1  # 幂（用于求所在位数）
        start_val = 10 ** power  # 起始值

        step = nth - start_count - 1  # 剩余移动步数
        step_length = i  # 每增一需要的步长
        # offset - 偏移值（从起始值开始）
        # pos - 结果值指向的位数 - 从最高位开始偏移
        offset, pos = divmod(step, step_length)

        curr_val = start_val + offset  # 当前数值 - 起始值 + 偏移值
        # 对应位数的数字，即解
        result = curr_val // 10 ** (power - pos) % 10

        return result


class Solution2(object):
    def findNthDigit(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 9:
            return n
        elif n == 10:
            return 1
        elif n == 11:
            return 0

        i, m = 1, 10
        while m < n:
            i += 1
            m += i * (9 * 10 ** (i - 1))
            print('loop', i, m)

        m -= i * (9 * 10 ** (i - 1))
        # print('val1', i, m)

        base = 10 ** (i - 1)
        offset, pos = divmod(n - m, i)
        # print('offset, pos', offset, pos)
        curr_val = base + offset

        res = curr_val // 10 ** ((i - 1) - pos) % 10

        # print('val2', curr_val, pos, res)

        return res
