
# 实现 int sqrt(int x) 函数。
#
# 计算并返回 x 的平方根，其中 x 是非负整数。
#
# 由于返回类型是整数，结果只保留整数的部分，小数部分将被舍去。
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/sqrtx
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
# refer: https://leetcode-cn.com/problems/search-insert-position/solution/te-bie-hao-yong-de-er-fen-cha-fa-fa-mo-ban-python-/

class Solution:
    def mySqrt(self, x: int) -> int:

        left = 0
        right = x

        while left < right:
            mid = (left + right + 1) >> 1
            square = mid * mid

            if square > x:
                right = mid - 1
            else:
                left = mid

        return left


if __name__ == '__main__':
    x = 8
    solution = Solution()
    m = solution.mySqrt(x)
    print(m)