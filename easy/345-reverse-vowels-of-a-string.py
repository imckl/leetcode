# 编写一个函数，以字符串作为输入，反转该字符串中的元音字母。
# https://leetcode-cn.com/problems/reverse-vowels-of-a-string/


class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = 'aeiouAEIOU'
        l, r = 0, len(s) - 1
        s = list(s)
        while l < r:
            if s[l] in vowels and s[r] in vowels:
                s[l], s[r] = s[r], s[l]
                l += 1
                r -= 1
            elif s[l] in vowels:
                r -= 1
            elif s[r] in vowels:
                l += 1
            else:
                l += 1
                r -= 1

        return ''.join(s)


class Solution3(object):
    def reverseVowels(self, s: str) -> str:
        vowels_index = [i for i, c in enumerate(s) if c in 'aeiouAEIOU']
        s_list = list(s)
        i, j = 0, len(vowels_index) - 1
        while i < j:
            s_list[vowels_index[i]], s_list[vowels_index[j]] = s_list[vowels_index[j]], s_list[vowels_index[i]]
            i += 1
            j -= 1
        return ''.join(s_list)


class Solution2(object):
    def __init__(self):
        self._vowels = ['a', 'i', 'o', 'u', 'e', 'A', 'I', 'O', 'U', 'E']

    def reverseVowels(self, s: str) -> str:
        vowels_index = [i for i, c in enumerate(s) if c in self._vowels]
        s_list = list(s)
        i, j = 0, len(vowels_index) - 1
        while i < j:
            s_list[vowels_index[i]], s_list[vowels_index[j]] = s_list[vowels_index[j]], s_list[vowels_index[i]]
            i += 1
            j -= 1
        return ''.join(s_list)
