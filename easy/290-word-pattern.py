# 给定一种规律 pattern 和一个字符串 str ，判断 str 是否遵循相同的规律。
#
# 这里的 遵循 指完全匹配，例如， pattern 里的每个字母和字符串 str 中的每个非空单词之间存在着双向连接的对应规律。
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/word-pattern
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。


class Solution(object):
    def wordPattern(self, pattern: str, str_: str) -> bool:
        str_list = str_.split()
        return list(map(pattern.find, pattern)) == list(map(str_list.index, str_list))


class Solution2(object):
    def wordPattern(self, pattern: str, str_: str) -> bool:
        pattern_index = [pattern.find(c) for c in pattern]
        str_list = str_.split()
        str_index = [str_list.index(s) for s in str_list]

        return pattern_index == str_index
