# 给定一个仅包含数字 2-9 的字符串，返回所有它能表示的字母组合。
# 给出数字到字母的映射如下（与电话按键相同）。注意 1 不对应任何字母。
# https://leetcode-cn.com/problems/letter-combinations-of-a-phone-number/

import itertools
import functools
from typing import List


class Solution(object):
    def __init__(self):
        self._lookup = {
            '2': 'abc', '3': 'def',
            '4': 'ghi', '5': 'jkl', '6': 'mno',
            '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
        }

    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        # 将数字转换为字母组合数组
        letter_list = (self._lookup[digit] for digit in digits)
        # 求字母组合数组的笛卡尔积
        result = [''.join(element) for element in itertools.product(*letter_list)]

        return result


def main():
    digits = '999999999'
    solution = Solution()
    result = solution.letterCombinations(digits)
    print(len(result))


if __name__ == '__main__':
    main()
