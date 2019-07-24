
# 给定两个有序整数数组 nums1 和 nums2，将 nums2 合并到 nums1 中，使得 num1 成为一个有序数组。
#
# 说明:
#
# 初始化 nums1 和 nums2 的元素数量分别为 m 和 n。
# 你可以假设 nums1 有足够的空间（空间大小大于或等于 m + n）来保存 nums2 中的元素。
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/merge-sorted-array
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        i, j = 0, 0
        l = []
        while i < m and j < n:
            if nums1[i] < nums2[j]:
                l.append(nums1[i])
                i += 1
            else:
                l.append(nums2[j])
                j += 1
        if i == m:
            l.extend(nums2[j:n])
        elif j == n:
            l.extend(nums1[i:m])
        nums1[:] = l

    def merge2(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        nums1[:] = sorted(nums1[:m] + nums2[:n])


if __name__ == '__main__':
    nums1 = [2, 3, 4, 7, 9, 9, 9]
    nums2 = [2, 3, 4, 5, 6, 8]
    solution = Solution()
    r = solution.merge(nums1, len(nums1), nums2, len(nums2))
    print(nums1)