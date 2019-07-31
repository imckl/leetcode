# Given two arrays, write a function to compute their intersection.
# https://leetcode.com/problems/intersection-of-two-arrays-ii/

from typing import List


class Solution(object):
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()
        result = []
        i = j = 0
        while i < len(nums1) and j < len(nums2):
            if nums1[i] == nums2[j]:
                result.append(nums1[i])
                i += 1
                j += 1
            elif nums1[i] < nums2[j]:
                i += 1
            else:
                j += 1
        return result


class Solution3(object):
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        dic = {}
        result = []
        for n in nums1:
            if n in dic:
                dic[n] += 1
            else:
                dic[n] = 1
        for n in nums2:
            if n in dic and dic[n] != 0:
                result.append(n)
                dic[n] -= 1
        return result


class Solution2(object):
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        dict1, dict2 = {}, {}
        for n in nums1:
            dict1[n] = 1 + (dict1[n] if n in dict1 else 0)

        for n in nums2:
            dict2[n] = 1 + (dict2[n] if n in dict2 else 0)

        result = []
        shared_nums = set(nums1) & set(nums2)

        for n in shared_nums:
            result.extend(map(lambda _: n, range(min(dict1[n], dict2[n]))))
            # result.extend([n for _ in range(min(dict1[n], dict2[n]))])

        return result
