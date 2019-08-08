# 给定一个数组 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。
#
# candidates 中的每个数字在每个组合中只能使用一次。
#
# 说明：
#
# 所有数字（包括目标数）都是正整数。
# 解集不能包含重复的组合。 
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/combination-sum-ii
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

from typing import List


class Solution:

    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        if not len(candidates):
            return []

        path = []
        result = []

        candidates.sort()

        self._combinationSum2(candidates, 0, len(candidates), target, path, result)
        print(len(result))
        return result

    def _combinationSum2(self, candidates: List[int], begin: int, size: int, target: int, path: List[int],
                         result: List[List[int]]):

        # 算术和等于target, 输出本次递归结果
        if target == 0:
            result.append(path[:])

        if begin == size:
            return

        for index in range(begin, size):

            if candidates[index] > target:
                break

            # 去重（剪枝）
            if index > begin and candidates[index - 1] == candidates[index]:
                continue

            path.append(candidates[index])

            self._combinationSum2(candidates, index + 1, size, target - candidates[index], path, result)

            path.pop()


class SolutionX:

    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        # sort before calculating
        candidates.sort()
        # list for storing result
        result = []

        for i in range(len(candidates)):

            # 去重(剪枝)
            # if i >= 1 and candidates[i] == candidates[i - 1]:
            #     continue

            # 排除剩余的运算(最小值大于target)
            if candidates[i] > target:
                return set(result)
            elif candidates[i] == target:
                result.append([candidates[i]])
                return set(result)

            sum_ = 0
            path = []
            path_index = []
            curr_index = i

            while True:

                sum_ += candidates[curr_index]
                path.append(candidates[curr_index])
                path_index.append(curr_index)

                # current index plus one
                curr_index += 1

                if sum_ == target:
                    result.append(path[:])
                    # 去重(剪枝)
                    while curr_index < len(candidates) and candidates[curr_index] == candidates[curr_index - 1]:
                        path_index[-1] = curr_index
                        curr_index += 1

                elif sum_ > target:
                    # rollback * 2
                    sum_ -= path.pop()
                    path_index.pop()

                    curr_index = path_index[-1] + 1
                    sum_ -= path.pop()
                    path_index.pop()

                if not path or not (0 <= curr_index <= len(candidates) - 1):
                    break

        return set(result)


def main():
    candidates = [10, 1, 2, 7, 6, 1, 5]
    target = 8

    candidates = [2, 5, 2, 1, 2]
    target = 5

    # candidates = [3, 1, 3, 5, 1, 1]
    # target = 8

    candidates = [4, 1, 1, 4, 4, 4, 4, 2, 3, 5]
    target = 10

    solution = Solution()
    result = solution.combinationSum2(candidates, target)
    print(result)


if __name__ == '__main__':
    main()
