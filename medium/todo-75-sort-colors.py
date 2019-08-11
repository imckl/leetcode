# Given an array with n objects colored red, white or blue, sort them in-place so that objects of
# the same color are adjacent, with the colors in the order red, white and blue.
#
# Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.
#
# Note: You are not suppose to use the library's sort function for this problem.
# https://leetcode.com/problems/sort-colors/

from typing import List


# 本解法的思路是沿着数组移动 curr 指针，若nums[curr] = 0，则将其与 nums[p0]互换；若 nums[curr] = 2 ，则与 nums[p2]互换。
class Solution:

    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        p0 = 0
        p2 = len(nums) - 1
        curr = 0

        while curr <= p2:

            if nums[curr] == 0:
                nums[curr], nums[p0] = nums[p0], nums[curr]
                p0 += 1
                curr += 1
            elif nums[curr] == 2:
                nums[curr], nums[p2] = nums[p2], nums[curr]
                p2 -= 1
            else:
                curr += 1


# 想法已经接近三指针，缺少值调换的思路
class SolutionX:

    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        blue_count = 0
        i = 0
        while i < len(nums):

            if nums[i] == 0:
                i += 1
                continue
            elif nums[i] == 1:
                nums.append(nums.pop(i))
                i += 1
            elif nums[i] == 2:
                nums.pop(i)
                blue_count += 1

        for i in range(blue_count):
            nums.append(2)


def main():
    nums = [2, 0, 2, 1, 1, 0]
    solution = Solution()
    result = solution.sortColors(nums)
    print(nums)


if __name__ == '__main__':
    main()


# 作者：gehui1007
# 链接：https://leetcode-cn.com/problems/two-sum/solution/ru-he-que-ding-qu-jian-de-kai-bi-by-gehui1007/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

# 其实有时候题目的基本思想大概都会，但就是会在一些边界的地方有些模糊，
# 比较典型的有二分查找的写法以及这个双指针(或者滑动窗口)的区间开闭的选择问题上，
# 基于本道题，我总结了以下四种不同的区间的写法，可能有些繁琐，但是我相信通过对比
# 各自的不同点会对如何确定区间开闭有着更深的体会。


# 以下有四种不同情况，但是共性是left左边都是封闭的(为0)，right右边都是封闭的(为len(nums)-1)
# 1.左闭右闭+左闭右闭
# 2.左闭右闭+左开右闭
# 3.左闭右开+左闭右闭
# 4.左闭右开加左开右闭
# 类似于三路快排

# 1.左闭右闭+左闭右闭
class Solution:
    def sortColors(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # 在迭代的过程中保持 nums[0..red] == 0,nums[red+1,i-1]==1,nums[blue,len(nums)-1]==2
        # nums[0..red] == 0,左闭右闭，所以red初始值为-1
        # i是用于循环nums中的元素的下标
        # nums[blue..n-1] == 2,左闭右闭，所以blue初始值为len(nums)
        red, i, blue = -1, 0, len(nums)
        # blue是左闭区间，所以这里是<,而不是<=
        while i < blue:
            if nums[i] == 1:
                i += 1
            elif nums[i] == 2:
                # 因为区间是左闭的，所以此时blue下标的值已经是2了，
                # 因此在把nums[i]和nums[blue]交换的时候，先把blue减1(blue-1这个位置还没定)
                blue -= 1
                nums[i], nums[blue] = nums[blue], nums[i]
                # 下面不需要i+=1
            else:  # nums[i] == 0
                # 使代码更严谨
                assert nums[i] == 0
                # 因为区间是右闭的，所以此时red下标的值已经是2了，
                # 因此在把nums[i]和nums[red]交换的时候，先把red加1(red+1这个位置还没定)
                red += 1
                nums[i], nums[red] = nums[red], nums[i]
                # 这里还需要i+=1
                i += 1


# 2.左闭右闭+左开右闭
class Solution:
    def sortColors(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # 在迭代的过程中保持 nums[0..red] == 0,nums[red+1,i-1]==1,nums[blue,len(nums)-1]==2
        # nums[0..red] == 0,左闭右闭，所以red初始值为-1
        # i是用于循环nums中的元素的下标
        # nums(blue..n-1] == 2,左开右闭，所以blue初始值为len(nums)-1
        red, i, blue = -1, 0, len(nums) - 1
        # blue是左开区间，所以这里是<=,而不是<
        while i <= blue:
            if nums[i] == 1:
                i += 1
            elif nums[i] == 2:
                # 因为区间是左开的，所以此时blue下标的值还没定
                # 因此先交换nums[i]和nums[blue]，再把blue减1
                nums[i], nums[blue] = nums[blue], nums[i]
                blue -= 1
            else:  # nums[i] == 0
                # 使代码更严谨
                assert nums[i] == 0
                # 因为区间是右闭的，所以此时red下标的值已经是2了，
                # 因此在把nums[i]和nums[red]交换的时候，先把red加1(red+1这个位置还没定)
                red += 1
                nums[i], nums[red] = nums[red], nums[i]
                # 这里还需要i+=1
                i += 1


# 3.左闭右开+左闭右闭
class Solution:
    def sortColors(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # 在迭代的过程中保持 nums[0..red] == 0,nums[red+1,i-1]==1,nums[blue,len(nums)-1]==2
        # nums[0..red) == 0,左闭右开，所以red初始值为0
        # i是用于循环nums中的元素的下标
        # nums[blue..n-1] == 2,左闭右闭，所以blue初始值为len(nums)
        red, i, blue = 0, 0, len(nums)
        # blue是左闭区间，所以这里是<,而不是<=
        while i < blue:
            if nums[i] == 1:
                i += 1
            elif nums[i] == 2:
                # 因为区间是左闭的，所以此时blue下标的值已经是2了，
                # 因此在把nums[i]和nums[blue]交换的时候，先把blue减1(blue-1这个位置还没定)
                blue -= 1
                nums[i], nums[blue] = nums[blue], nums[i]
                # 下面不需要i+=1
            else:  # nums[i] == 0
                # 使代码更严谨
                assert nums[i] == 0
                # 因为区间是右开的，所以此时red下标的值还没定
                # 因此先交换nums[i]和nums[red]，再把red加1
                nums[i], nums[red] = nums[red], nums[i]
                red += 1
                i += 1


# 4.左闭右开加左开右闭
class Solution:
    def sortColors(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # num[0..red) == 0,左闭右开，所以red初始值为0
        # i是用于循环nums中的元素的下标
        # num(blue..n-1] == 2,左开右闭，所以blue初始值为len(nums) - 1
        red, i, blue = 0, 0, len(nums) - 1
        # blue是左开区间，所以这里是<=,而不是<
        while i <= blue:
            if nums[i] == 1:
                i += 1
            elif nums[i] == 2:
                # 因为区间是左开的，所以此时blue下标的值还没定
                # 因此先交换nums[i]和nums[blue]，再把blue减1
                nums[i], nums[blue] = nums[blue], nums[i]
                blue -= 1
            else:
                assert nums[i] == 0
                # 因为区间是右开的，所以此时red下标的值还没定
                # 因此先交换nums[i]和nums[red]，再把red加1
                nums[red], nums[i] = nums[i], nums[red]
                i += 1
                red += 1
