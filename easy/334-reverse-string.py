# 编写一个函数，其作用是将输入的字符串反转过来。输入字符串以字符数组 char[] 的形式给出。
#
# 不要给另外的数组分配额外的空间，你必须原地修改输入数组、使用 O(1) 的额外空间解决这一问题。
#
# 你可以假设数组中的所有字符都是 ASCII 码表中的可打印字符。
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/reverse-string
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

from typing import List


class Solution(object):
    def reverseString(self, s: List[str]):
        s[:] = s[::-1]


class Solution2(object):
    def reverseString(self, s: List[str]):
        left = 0
        right = len(s) - 1
        mid = (left + right) >> 1

        for i in range(mid + 1):
            s[i], s[-1 - i] = s[-1 - i], s[i]
