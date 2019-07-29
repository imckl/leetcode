
# 给定一个整数 n，返回 n! 结果尾数中零的数量。
# https://leetcode-cn.com/problems/factorial-trailing-zeroes/


class Solution(object):
    def trailingZeroes(self, n: int) -> int:
        result = 0

        while n > 0:
            result += n // 5
            n //= 5

        return result


class Solution2(object):
    def trailingZeroes(self, n: int) -> int:
        """
        :type n: int
        :rtype: int
        """
        result = 0
        base, power = 5, 0

        while True:
            power += 1
            divisor = base ** power
            quotient, remainder = divmod(n, divisor)

            if quotient == 0 and remainder == n:
                break

            result += quotient

        return result



def main():
    n = 500
    solution = Solution()
    result = solution.trailingZeroes(n)
    print(result)


if __name__ == '__main__':
    main()
