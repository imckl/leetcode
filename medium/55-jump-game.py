# 给定一个非负整数数组，你最初位于数组的第一个位置。
# 数组中的每个元素代表你在该位置可以跳跃的最大长度。
# 判断你是否能够到达最后一个位置。
# https://leetcode-cn.com/problems/jump-game/

from typing import List


class Solution:

    def canJump(self, nums: List[int]) -> bool:

        # 如果没有可移动步数为零，则一定能到最后一个位置
        if 0 not in nums:
            return True

        size = len(nums)
        curr_idx = 0

        while curr_idx < size:

            # 到达最后一个值
            if curr_idx == size - 1:
                return True

            # 如果当前位置可移动步数为零，则无法到达最后一个位置
            if nums[curr_idx] == 0:
                return False

            # 当前移动步数范围
            available_move = nums[curr_idx]
            # 当前移动步数范围内，行动两次可以到达的最大距离
            max_step = 0
            # 上述情况实际移动的步数
            actual_move = 0
            # 移动步数（最小一步，最大available_move步）
            for move in range(1, available_move + 1):

                # 当前移动步数超过数组长度，说明可到达最后一个值
                tmp_idx = move + curr_idx
                if tmp_idx > size - 1:
                    return True

                # 当前移动步数，行动两次的最大移动距离
                # 如果当前的最大距离比记录的最大距离大，则更新最大移动距离和满足要求的当前移动步数
                tmp_max_step = nums[tmp_idx] + move
                if tmp_max_step > max_step:
                    max_step = tmp_max_step
                    actual_move = move

            # 移动actual_move步
            curr_idx = curr_idx + actual_move

        return True


def main():
    nums = [2, 3, 1, 1, 4]
    # nums = [3, 1, 0, 0, 0]
    nums = [1, 2, 0, 1]
    # nums = [3, 0, 0, 0]
    solution = Solution()
    result = solution.canJump(nums)
    print(result)


if __name__ == '__main__':
    main()
