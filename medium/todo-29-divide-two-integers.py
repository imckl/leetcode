# 给定两个整数，被除数 dividend 和除数 divisor。将两数相除，要求不使用乘法、除法和 mod 运算符。
#
# 返回被除数 dividend 除以除数 divisor 得到的商。
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/divide-two-integers
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。


class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        int_max = 2 ** 31 - 1
        int_min = -2 ** 31

        str_dividend = str(dividend)
        for char in str_dividend:
            digit = int(char)
            if digit < divisor:
                pass



def main():
    dividend = 2 ** 31 - 1
    divisor = 2
    solution = Solution()
    result = solution.divide(dividend, divisor)
    print(result)


if __name__ == '__main__':
    main()
