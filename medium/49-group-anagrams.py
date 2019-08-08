# 给定一个字符串数组，将字母异位词组合在一起。字母异位词指字母相同，但排列不同的字符串。
# https://leetcode-cn.com/problems/group-anagrams/

from typing import List, Tuple
from itertools import groupby
import operator
from collections import Counter
from collections import defaultdict


class SolutionXX:

    def groupAnagrams(self, words: List[str]) -> List[List[str]]:
        rules = {
            'a': 2, 'b': 3, 'c': 5, 'd': 7, 'e': 11,
            'f': 13, 'g': 17, 'h': 19, 'i': 23, 'j': 29,
            'k': 31, 'l': 41, 'm': 43, 'n': 47, 'o': 53,
            'p': 59, 'q': 61, 'r': 67, 's': 71, 't': 73,
            'u': 79, 'v': 83, 'w': 89, 'x': 97, 'y': 101,
            'z': 103}

        groups = defaultdict(list)
        for word in words:
            key = 1
            for letter in word:
                key *= rules[letter]
            groups[key].append(word)

        return groups.values()


class Solution3:

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        result = defaultdict(list)
        for str_ in strs:
            count = [0] * 26
            for char in str_:
                count[ord(char) - ord('a')] += 1

            result[tuple(count)].append(str_)

        return result.values()


class Solution2:

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = []
        diff = [[str_, sorted(str_)] for str_ in strs]
        diff.sort(key=operator.itemgetter(1))
        for _, items in groupby(diff, key=operator.itemgetter(1)):
            result.append([i[0] for i in items])

        return result


class SolutionX:

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = []

        diff = [(sum(ord(c) for c in str_), len(str_), i) for i, str_ in enumerate(strs)]
        diff.sort(key=operator.itemgetter(0, 1, 2))
        groups = groupby(diff, key=operator.itemgetter(0, 1))

        for _, items in groups:
            result.append([strs[i] for i in map(lambda n: n[2], items)])

        return result


def main():
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    solution = Solution()
    result = solution.groupAnagrams(strs)
    print(result)


if __name__ == '__main__':
    main()
