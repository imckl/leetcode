# 给定一个包含大写字母和小写字母的字符串，找到通过这些字母构造成的最长的回文串。
# 在构造过程中，请注意区分大小写。比如 "Aa" 不能当做一个回文字符串。
# https://leetcode-cn.com/problems/longest-palindrome/

from collections import Counter


class Solution3(object):
    def longestPalindrome(self, s: str) -> int:
        counter = {c: s.count(c) for c in set(s)}  # 字符计数集
        return sum(count >> 1 << 1 for count in counter.values()) + \
               (1 if any(count & 1 for count in counter.values()) else 0)


class Solution(object):

    def longestPalindrome(self, s: str) -> int:
        counter = Counter(s)  # 字符计数集

        # 累加每个字符个数的最大偶数，最终结果为回文串最大长度
        palindrome_length = sum(count >> 1 << 1 for count in counter.values())

        # 是否存在任意字符个数为奇数个；如果存在，则需要增一到回文串最大长度上
        add_odd = 1 if any(count & 1 for count in counter.values()) else 0

        # 返回回文串最大长度
        return palindrome_length + add_odd


class Solution2(object):

    def longestPalindrome(self, s: str) -> int:
        palindrome_length = 0
        dic = {c: s.count(c) for c in set(s)}
        has_odd = any(count % 2 == 1 for count in dic.values())

        for count in dic.values():
            palindrome_length += count // 2 * 2

        return palindrome_length + (1 if has_odd else 0)
