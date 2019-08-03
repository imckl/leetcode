# 给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为 1000。
# https://leetcode-cn.com/problems/longest-palindromic-substring/

from typing import Tuple


class Solution(object):

    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ''

        result_left, result_right = 0, 0

        for i, c in enumerate(s):
            start, end = max(self._expand_around(s, i, i), self._expand_around(s, i, i + 1),
                             key=lambda x: x[1] - x[0])
            if end - start > result_right - result_left:
                result_left, result_right = start, end

        return s[result_left:result_right]

    def _expand_around(self, s: str, mid_left: int, mid_right: int) -> Tuple[int, int]:
        left, right = mid_left, mid_right
        while left >= 0 and right <= len(s) - 1 and s[left] == s[right]:
            left -= 1
            right += 1
        return left + 1, right - 1 + 1


def main():
    s = 'abcdefg'
    s = 'abcddcbaa'
    s = 'cbbca'
    solution = Solution()
    m = solution.longestPalindrome(s)
    print(m)


if __name__ == '__main__':
    main()
