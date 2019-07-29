# Given two strings s and t , write a function to determine if t is an anagram of s.
# https://leetcode.com/problems/valid-anagram/


class Solution(object):
    def isAnagram(self, s: str, t: str) -> bool:
        s_compose, t_compose = {}, {}

        for i in s:
            s_compose[i] = s_compose[i] + 1 if i in s_compose else 1

        for i in t:
            t_compose[i] = t_compose[i] + 1 if i in t_compose else 1

        return t_compose == s_compose
