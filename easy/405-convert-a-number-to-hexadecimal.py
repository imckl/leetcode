# Given an integer, write an algorithm to convert it to hexadecimal.
# For negative integer, two’s complement method is used.
#
# Note:
#
# All letters in hexadecimal (a-f) must be in lowercase.
# The hexadecimal string must not contain extra leading 0s. If the number is zero, it is represented by
# a single zero character '0'; otherwise, the first character in the hexadecimal string will not be the zero character.
# The given number is guaranteed to fit within the range of a 32-bit signed integer.
# You must not use any method provided by the library which converts/formats the number to hex directly.
# https://leetcode.com/problems/convert-a-number-to-hexadecimal/


class Solution(object):

    def toHex(self, num: int) -> str:
        # 如果小于零，则进行补码
        max_int = 0xffffffff + 0x00000001
        if num < 0:
            num += max_int

        hex_convert = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f')
        divisor = 0x00000010        # 除数
        result = ''                 # 结果

        # do...while
        # 按照运算规则取模，并构造结果字符串
        quotient, remainder = divmod(num, divisor)
        result = hex_convert[remainder] + result
        while True:
            quotient, remainder = divmod(quotient, divisor)
            if not (quotient == remainder == 0):
                result = hex_convert[remainder] + result
            else:
                break

        return result
