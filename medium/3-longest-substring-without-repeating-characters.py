# 给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为 1000。
# https://leetcode-cn.com/problems/longest-palindromic-substring/


# #### 备注一：
#  1. 假设有字符串``"abbcda"``, 观察可知最长不重复子串为``"bcda"``
#  2. 根据编写的算法，在刚遍历至最后一个``'a'``时，dic['a']的值为0，此时start的值已经更新为索引``1``，索引``1``以及之前的字符都是存在重复，不用再在运算中考虑的字符。
#  3. ``ignore_index_end``的注释，是``可抛弃字符串的索引尾值``，是双指针方法中左指针（起始针）的反面;
#  4. 如果仍然不好理解，可以做到理解双指针法也行，毕竟ignore_index_end的确有点绕...
class Solution(object):
    def lengthOfLongestSubstring(self, s: str) -> int:
        # 可抛弃字符串的索引尾值 - 字符串索引值，该索引值以及之前的字符都属于重复字符串中的一部分，不再在计算中涉及
        ignore_index_end = -1
        dic = {}        # 任意字符最后出现在索引的位置 - {字符: 字符索引值}
        max_length = 0  # 最长字符串长度

        for i, c in enumerate(s):
            # 如果字典中已经存在字符c，则字符c重复
            # 如果字符索引值大于ignore_index_end，则字符c在需处理的范围内（补充说明请参考备注一）
            if c in dic and dic[c] > ignore_index_end:
                # 先更新可抛弃字符串的索引尾值为字符c上一次的索引值
                ignore_index_end = dic[c]
                # 再更新字符c的索引值
                dic[c] = i
            # 否则，
            else:
                # 更新字符最近的索引位置
                dic[c] = i
                # 更新最大长度
                max_length = max(i - ignore_index_end, max_length)

        return max_length


# 改进：使用双指针
class Solution4(object):

    def lengthOfLongestSubstring(self, s: str) -> int:
        # 字符串为空则返回零
        if not s:
            return 0

        max_length = 0      # 滑动窗口数组
        left, right = 0, 0  # 双指针

        for i, c in enumerate(s):
            # 如果字符不在滑动窗口中，则直接扩展窗口
            if c not in s[left:right]:
                # 右指针右移一位
                right += 1
            # 如果字符在滑动窗口中，则
            # 1. 从窗口中移除重复字符及之前的字符串部分
            # 2. 再扩展窗口
            else:
                # 在滑动窗口范围内中找出对应的首个字符的索引X，对应的新的左指针位置为X + 1
                # 左指针右移 索引X增一 位
                left = s[left:right].index(c) + 1 + left
                # 右指针增一
                right += 1

            # 更新最大长度
            max_length = max(right - left, max_length)

        # 如果最大长度不为零，返回最大长度
        # 如果最大长度仍为零，则说明遍历整个字符串都没有发现重复字符，最大长度即为字符串本很的长度
        return max_length if max_length != 0 else len(s)


class Solution3(object):

    def lengthOfLongestSubstring(self, s: str) -> int:
        # 字符串为空则返回零
        if not s:
            return 0

        window = []     # 滑动窗口数组
        max_length = 0  # 最长串长度

        # 遍历字符串
        for c in s:
            # 如果字符不在滑动窗口中，则直接扩展窗口
            if c not in window:
                # 使用当前字符扩展窗口
                window.append(c)
            # 如果字符在滑动窗口中，则
            # 1. 从窗口中移除重复字符及之前的字符串部分
            # 2. 再扩展窗口
            else:
                # 从窗口中移除重复字符及之前的字符串部分，新字符串即为无重复字符的字符串
                window[:] = window[window.index(c) + 1:]
                # 扩展窗口
                window.append(c)

            # 更新最大长度
            max_length = max(len(window), max_length)

        # 如果最大长度不为零，返回最大长度
        # 如果最大长度仍为零，则说明遍历整个字符串都没有发现重复字符，最大长度即为字符串本很的长度
        return max_length if max_length != 0 else len(s)


def main():
    s = 'abcdefg'
    s = 'abcddcbaa'
    s = 'cbbca'
    solution = Solution()
    m = solution.lengthOfLongestSubstring(s)
    print(m)


if __name__ == '__main__':
    main()
