
# 给定一个正整数，返回它在 Excel 表中相对应的列名称。
# https://leetcode-cn.com/problems/excel-sheet-column-title/


class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        result = []

        divisor = 26
        dividend = n

        quotient = dividend
        while True:
            quotient, remainder = divmod(quotient, divisor)

            print(quotient, remainder)

            if quotient <= 0 and remainder == 0:
                break

            if remainder == 0:
                result.append(26)
                quotient -= 1
            else:
                result.append(remainder)

        result = result[::-1]
        mapping = lambda x: chr(x + 64) if x >= 1 else ''
        # return result
        return ''.join([mapping(i) for i in result])


if __name__ == '__main__':
    # num = 26 ** 3
    num = 26 ** 2
    num = 1352
    solution = Solution()
    result = solution.convertToTitle(num)
    print(result)
