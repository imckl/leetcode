
# 给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为 1000。
# https://leetcode-cn.com/problems/longest-palindromic-substring/


class Solution:
    def longestPalindrome(self, s: str) -> str:
        longest_start, longest_end = 0, 0
        for i in range(len(s)):
            for j in range(1, i + 1):
                try:
                    print(i-j, i+j, len(s))
                    m = s[i - j]
                    n = s[i + j]
                    print(m, n)
                    if m == n:
                        start = i - j
                        end = i + j
                        if end - start > longest_end - longest_start:
                            longest_end = end
                            longest_start = start
                    else:
                        break
                except IndexError:
                    continue
        print(longest_start, longest_end, s[longest_start:longest_end + 1])


if __name__ == '__main__':
    s = 'abcdefg'
    s = 'abcddcbaa'
    s = 'cbbca'
    solution = Solution()
    m = solution.longestPalindrome(s)
    print(m)