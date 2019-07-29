
# Given a column title as appear in an Excel sheet, return its corresponding column number.
# https://leetcode.com/problems/excel-sheet-column-number/


class Solution(object):
    def titleToNumber(self, s: str) -> int:
        """
        :type s: str
        :rtype: int
        """
        factor = 26
        result = 0
        char_to_int = lambda c: ord(c) - 64
        for i, c in enumerate(s[::-1]):
            n = char_to_int(c)
            result += n * factor ** i
        return result
