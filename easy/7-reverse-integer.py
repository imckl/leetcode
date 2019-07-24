
# https://leetcode.com/problems/reverse-integer/
# Given a 32-bit signed integer, reverse digits of an integer.


class Solution:
    def reverse(self, x: int) -> int:
        m = int(str(int(abs(x)))[::-1])
        m = m if x > 0 else -m
        return m if -2 ** 31 <= m <= 2 ** 31 - 1 else 0


if __name__ == '__main__':
    x = 1534236469
    s = Solution()
    print(s.reverse(x))