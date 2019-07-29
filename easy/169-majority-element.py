
# Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.
#
# You may assume that the array is non-empty and the majority element always exist in the array.
# https://leetcode.com/problems/majority-element/

from typing import List
import collections


class Solution:
    def majorityElement(self, nums):
        count = 0
        candidate = None

        for num in nums:
            if count == 0:
                candidate = num
            count += (1 if num == candidate else -1)

        return candidate


class Solution3(object):
    def majorityElement(self, nums: List[int]):
        """
        :type nums: List[int]
        :rtype: int
        """
        counts = collections.Counter(nums)
        return max(counts.keys(), key=counts.get)


class Solution2(object):
    def majorityElement(self, nums: List[int]):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        return nums[len(nums) // 2]


def main():
    nums = [5, 7, 7, 5, 7, 1, 7]
    solution = Solution()
    result = solution.majorityElement(nums)
    print(result)

if __name__ == '__main__':
    main()