
# https://leetcode-cn.com/problems/longest-substring-without-repeating-characters/
# 给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start, end = 0, 0
        length = len(s)

        for i in range(len(s)):
            s.index()




if __name__ == '__main__':
    s = 'abcddefgab'