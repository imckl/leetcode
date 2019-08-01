# 给定一个赎金信 (ransom) 字符串和一个杂志(magazine)字符串，判断第一个字符串ransom能不能由第二个字符串magazines里面的字符构成。如果可以构成，返回 true ；否则返回 false。
#
# (题目说明：为了不暴露赎金信字迹，要从杂志上搜索各个需要的字母，组成单词来表达意思。)
#
# 注意：
#
# 你可以假设两个字符串均只含有小写字母。
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/ransom-note
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
# https://leetcode-cn.com/problems/ransom-note/


# Time: O(N)
# Space: O(1)
class Solution(object):
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        for c in ransomNote:
            if c in magazine:
                magazine = magazine.replace(c, '', 1)
            else:
                return False
        return True


# Time: O(N)
# Space: O(1)
class Solution2(object):
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        magazine_dict = {}
        for c in magazine:
            if c in magazine_dict:
                magazine_dict[c] += 1
            else:
                magazine_dict[c] = 1

        for c in ransomNote:
            if c in magazine_dict and magazine_dict[c] > 0:
                magazine_dict[c] -= 1
            else:
                return False

        return True
