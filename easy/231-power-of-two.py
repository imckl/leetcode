# Given an integer, write a function to determine if it is a power of two.
# https://leetcode.com/problems/power-of-two/


class Solution(object):
    def isPowerOfTwo(self, n: int) -> bool:
        return n > 0 and n & (n - 1) == 0


class Solution2(object):
    def isPowerOfTwo(self, n: int) -> bool:
        if n == 0:
            return False

        while n != 1:
            if n & 1:
                return False
            n >>= 1
        return True
