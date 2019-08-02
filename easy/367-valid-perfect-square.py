# 给定一个正整数 num，编写一个函数，如果 num 是一个完全平方数，则返回 True，否则返回 False。
#
# 说明：不要使用任何内置的库函数，如  sqrt。
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/valid-perfect-square
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。


# 时间复杂度：O(logN)
# 空间复杂度：O(1)
class Solution(object):
    def isPerfectSquare(self, num: int) -> bool:
        # 题设num为正整数，因此起始值为1
        # 结束值为num
        left, right = 1, num
        while left < right:
            mid = (left + right + 1) >> 1
            if mid * mid > num:
                right = mid - 1
            else:
                left = mid
        return left * left == num



class Solution3(object):
    def isPerfectSquare(self, num: int) -> bool:
        i = 1
        while num > 0:
            num -= i
            i += 2
        return num == 0


class Solution2(object):
    def isPerfectSquare(self, num: int) -> bool:
        n = 0
        while True:
            pow_n = n * n
            if pow_n > num:
                return False
            elif pow_n == num:
                return True
            n += 1
