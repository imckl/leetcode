
# https://leetcode-cn.com/problems/count-and-say/
# 报数序列是一个整数序列，按照其中的整数的顺序进行报数，得到下一个数。其前五项如下：

import re


class Solution:
    def countAndSay(self, n: int) -> str:
        result = '1'

        for _ in range(n - 1):
            result = self._countAndSay(result)

        return result

    def _countAndSay(self, s: str) -> str:
        count = 1
        result = ''

        for i in range(len(s)):
            try:
                if s[i] == s[i + 1]:
                    count += 1
                else:
                    result += str(count) + s[i]
                    count = 1
            except IndexError:
                result += str(count) + s[i]

        return result

    def countAndSay2(self, n):
        s = '1'
        for _ in range(n - 1):
            s = re.sub(r'(.)\1*', lambda m: str(len(m.group(0))) + m.group(1), s)
        return s


if __name__ == '__main__':
    solution = Solution()
    m = solution.countAndSay2(50)
    # print(m)
