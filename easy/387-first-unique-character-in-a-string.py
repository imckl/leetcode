# Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.
# https://leetcode.com/problems/first-unique-character-in-a-string/

from collections import OrderedDict
from collections import Counter


class Solution(object):
    def firstUniqChar(self, s):
        # 先假设最小索引为最后的字符索引
        min_unique_char_index = len(s)

        # 已知字符串由小写字母构成，则遍历a-z
        for c in "abcdefghijklmnopqrstuvwxyz":
            i = s.find(c)
            # 分别从目标的字符串头和字符串尾查找对应字母的索引；如果两索引相等，则说明是单一字符
            if i != -1 and i == s.rfind(c):
                # 更新最新的最小索引
                min_unique_char_index = min(min_unique_char_index, i)

        # 如果返回值不为最后字符的索引，则返回最小索引值
        # 否则，根据题意，返回-1
        return min_unique_char_index if min_unique_char_index != len(s) else -1


class Solution5(object):

    def firstUniqChar(self, s: str) -> int:
        # 计算字符出现次数
        dic = {c: s.count(c) for c in set(s)}
        # 找到并返回首个满足出现次数为一的字符
        for i, c in enumerate(s):
            if dic[c] == 1:
                return i

        return -1


class Solution4(object):

    def firstUniqChar(self, s: str) -> int:
        count = Counter(s)

        for i, c in enumerate(s):
            if count[c] == 1:
                return i

        return -1


class Solution3(object):

    def firstUniqChar(self, s: str) -> int:
        dic = {}

        # 记录字符出现次数
        for c in s:
            dic[c] = dic[c] + 1 if c in dic else 1

        # 过滤出现次数不为一的字符
        unique_chars = [k for k, v in filter(lambda kvp: kvp[1] == 1, dic.items())]
        # 遍历目标字符串，返回首个出现在unique_chars中的字符的索引
        for i, c in enumerate(s):
            if c in unique_chars:
                return i

        return -1


class Solution2(object):

    def firstUniqChar(self, s: str) -> int:
        odict = OrderedDict()

        # 记录字符出现次数
        for c in s:
            odict[c] = odict[c] + 1 if c in odict else 1

        # 利用有序的特性，在字典中找出首个出现次数为一的字符串
        for k, v in odict.items():
            if v == 1:
                # 返回字符串首次出现的位置
                return s.index(k)

        return -1
