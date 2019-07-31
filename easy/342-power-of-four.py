# Given an integer (signed 32 bits), write a function to check whether it is a power of 4.
# https://leetcode.com/problems/power-of-four/


class Solution(object):
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num == 1:
            return True
        if num < 4:
            return False

        return num & (num - 1) == 0 and num % 3 == 1


class Solution2(object):
    def isPowerOfFour(self, num: int) -> bool:
        if num == 1:
            return True
        if num < 4:
            return False
        bin_str = bin(num)[3:]
        return len(bin_str) % 2 == 0 and int(bin_str) == 0
