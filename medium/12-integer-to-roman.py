# https://leetcode-cn.com/problems/integer-to-roman/


class Solution(object):

    def __init__(self):
        self._rules = (
            ('M', 1000),
            ('CM', 900), ('D', 500), ('CD', 400), ('C', 100),
            ('XC', 90), ('L', 50), ('XL', 40), ('X', 10),
            ('IX', 9), ('V', 5), ('IV', 4), ('I', 1),
        )

    def intToRoman(self, num: int) -> str:
        result = []

        for roman, dec in self._rules:
            if num >= dec:
                result.extend([roman] * (num // dec))
                num %= dec

        return ''.join(result)


def main():
    num = 3998
    solution = Solution()
    n = solution.intToRoman(num)
    print(n)


if __name__ == '__main__':
    main()
