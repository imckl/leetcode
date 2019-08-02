
# 给定两个字符串 s 和 t，它们只包含小写字母。
# 字符串 t 由字符串 s 随机重排，然后在随机位置添加一个字母。
# 请找出在 t 中被添加的字母。
# https://leetcode-cn.com/problems/find-the-difference/


class Solution(object):
    def findTheDifference(self, s: str, t: str) -> str:
        n = 0
        for c in s:
            n ^= ord(c)
        for c in t:
            n ^= ord(c)
        return ascii(n)
