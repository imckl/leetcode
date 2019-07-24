
# https://leetcode.com/problems/palindrome-number/
# Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.


class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        l = self._get_len(x)
        m, n = 0, l - 1
        while m < n:
            if x // 10 ** n % 10 != x // 10 ** m % 10:
                return False
            m += 1
            n -= 1
        return True

    def _get_len(self, x: int) -> int:
        i = 0
        while abs(x) >= 10 ** i:
            i += 1
        return i


if __name__ == '__main__':
    x = 0
    s = Solution()
    m = s.isPalindrome(x)
    print(m)
