# 给定两个以字符串形式表示的非负整数 num1 和 num2，返回 num1 和 num2 的乘积，它们的乘积也表示为字符串形式。
# https://leetcode-cn.com/problems/multiply-strings/


class Solution:

    def multiply(self, num1: str, num2: str) -> str:
        rules = {
            '0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9
        }

        n1 = 0
        for i, char in enumerate(num1[::-1]):
            n1 += rules[char] * 10 ** i

        n2 = 0
        for i, char in enumerate(num2[::-1]):
            n2 += rules[char] * 10 ** i

        return str(n1 * n2)


def main():
    num1 = '123'
    num2 = '456'
    solution = Solution()
    result = solution.multiply(num1, num2)
    print(result)


if __name__ == '__main__':
    main()
