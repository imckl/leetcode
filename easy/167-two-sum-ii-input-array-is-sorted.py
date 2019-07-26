
# Given an array of integers that is already sorted in ascending order, find two numbers such that they add up to a specific target number.
#
# The function twoSum should return indices of the two numbers such that they add up to the target, where index1 must be less than index2.
#
# Note:
#
# Your returned answers (both index1 and index2) are not zero-based.
# You may assume that each input would have exactly one solution and you may not use the same element twice.
# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/


class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        length = len(numbers)

        for i in range(length):
            t = target - numbers[i]
            left = i
            right = length - 1

            while left < right:
                mid = (left + right + 1) >> 1
                if numbers[mid] > target:
                    right = mid - 1
                else:
                    left = mid
            if numbers[left] == t:
                return [i + 1, left + 1]

        return []


class Solution3(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        dic = {}

        for i, num in enumerate(numbers):
            if target - num in dic:
                return [dic[target - num] + 1, i + 1]
            dic[num] = i


class Solution2(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        i, j = 0, len(numbers) - 1

        while i < j:
            sum_ = numbers[i] + numbers[j]
            if sum_ > target:
                j -= 1
            elif sum_ < target:
                i += 1
            else:
                return [i, j]

        return []


if __name__ == '__main__':
    numbers = [-1, 0]
    target = -1
    solution = Solution()
    r = solution.twoSum(numbers, target)
    print(r)
