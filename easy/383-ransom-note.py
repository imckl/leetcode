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


# 检查ransomNote的每个字符是否在magazine字符串中:
# 如果在则在maazine中移除该一个字符串；
# 如果不在，则无法构成，返回False
# 时间复杂度: O(N) 空间复杂度: O(1)
class Solution(object):
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        for c in ransomNote:
            if c in magazine:
                magazine = magazine.replace(c, '', 1)
            else:
                return False
        return True


# 1. 用哈希表存储magazine字符及个数
# 2. 遍历ransomNote:
#   2.1. 如果哈希表中有该字符并且字符计数大于零，说明仍能由magzine构成，此时对应的字符计数减一
#   2.2. 否则，无法构成，返回False
# 时间复杂度: O(N) 空间复杂度: O(N)
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
