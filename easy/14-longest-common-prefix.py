
# https://leetcode.com/problems/longest-common-prefix/
# Write a function to find the longest common prefix string amongst an array of strings.

from typing import List


class Solution:
    def longestCommonPrefix(self, strs:List[str]) -> str:
        if len(strs) <= 0:
            return ''
        elif len(strs) == 1:
            return strs[0]

        strs.sort(key=lambda s: (len(s)))

        for i in range(len(strs[0]), 0, -1):
            has = False
            for s in strs[1:]:
                if strs[0][:i] != s[:i]:
                    has = False
                    break
                else:
                    has = True
            if has:
                return strs[0][:i]
        return ''

    def longestCommonPrefix_trunc3(self, strs:List[str]) -> str:
        if len(strs) <= 0:
            return ''

        strs.sort(key=lambda s: (len(s), s))

        for i in range(len(strs[0]), 0, -1):
            has = False
            for s in strs[1:]:
                if strs[0][:i] not in s:
                    has = False
                    break
                else:
                    has = True
            if has:
                return strs[0][:i]
        return ''


    def longestCommonPrefix_trunc2(self, strs: List[str]) -> str:
        if len(strs) <= 0:
            return ''
        elif len(strs) == 1:
            return strs[0]

        strs.sort(key=lambda s: len(s))
        # for i in range(len(strs[0]), 0, -1):
        for i in range(len(strs[0])):
            has = False
            # print(strs[0][i:])
            for s in strs[1:]:
                print(strs[0][i:], s)
                if strs[0][i:] not in s:
                    has = False
                    break
                else:
                    has = True
            if has:
                return strs[0][i:]

        for i in range(len(strs[0]), 0, -1):
            has = False
            for s in strs[1:]:
                if strs[0][:i] not in s:
                    has = False
                    break
                else:
                    has = True
            if has:
                return strs[0][:i]
        return ''

    def longestCommonPrefix_trunc(self, strs: List[str]) -> str:
        if len(strs) <= 0:
            return ''

        r = ''
        str_min_len = min(len(s) for s in strs)
        for i in range(str_min_len):
            c = strs[0][i]
            r += c
            for s in strs[1:]:
                if s[i] != c:
                    r = r[:-1]
        return r


if __name__ == '__main__':
    strs = ["flower","flower","flower"]
    strs = ["flower","flow","flight"]
    # strs = ["dogr","racecar","car"]
    # strs = ["flower","flow","flight"]
    # strs = ["", "", ""]
    # strs = ["abcdehgfg", "jhg"]
    # strs = ['aracecar', 'dogr', 'carewrwewr']

    s = Solution()
    r = s.longestCommonPrefix(strs)
    print(r)