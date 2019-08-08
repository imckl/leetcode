# 给定一个无重复元素的数组 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。
#
# candidates 中的数字可以无限制重复被选取。
#
# 说明：
#
# 所有数字（包括 target）都是正整数。
# 解集不能包含重复的组合。 
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/combination-sum
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

from typing import List


class Solution:

    def __init__(self):
        self._result = []

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

        if not len(candidates):
            return []

        # 在遍历的过程中记录路径，一般而言它是一个栈
        path = []

        # 剪枝的前提是数组元素排序
        # 深度深的边不能比深度浅的边还小
        # 要排序的理由：1、前面用过的数后面不能再用；2、下一层边上的数不能小于上一层边上的数。
        candidates.sort()

        self._combinationSum(candidates, 0, len(candidates) - 1, path, target, 0)

        return self._result

    def _combinationSum(self, candidates: List[int], begin: int, end: int,
                        path: List[int], target: int, sum_: int):

        # 算术和等于target, 输出本次递归结果
        if sum_ == target:
            self._result.append(path[:])

        for index in range(begin, end + 1):

            # 先写递归中止（不满足递归继续）的情况
            # 如果算术和大于target，本次递归中止
            # 这里是特意使用tmp_sum的，强调添加候选数和求和是一起进行的操作，对刚了解回溯算法的coder也许会更友好？
            tmp_sum = sum_ + candidates[index]
            if tmp_sum > target:
                break

            # 满足递归继续的条件
            # 添加当前候选数，求算术和
            path.append(candidates[index])
            sum_ = tmp_sum

            # 因为下一层不能比上一层还小，索引起始还是从 index 开始
            self._combinationSum(candidates, index, end, path, target, sum_)

            # 当前递归结束，两种情况：1. 正常结束；2. 提前中止
            # 删除当前候选数，求算术和
            path.pop()
            sum_ -= candidates[index]



class SolutionX2:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        stack = []
        candidates.sort()
        result = []

        for i in range(len(candidates)):

            # 当前值等于或大于target时，则后续遍历值必定大于target，直接跳出循环
            if candidates[i] == target:
                result.append([candidates[i]])
                break
            elif candidates[i] > target:
                break

            sum_ = float('-inf')
            curr_idx = i

            while stack or sum_ == float('-inf'):

                if curr_idx == len(candidates):
                    curr_idx = i + 1

                stack.append(candidates[curr_idx])
                sum_ = sum_ + candidates[curr_idx] if sum_ != float('-inf') else candidates[curr_idx]

                if sum_ == target:
                    result.append(stack[:])
                    sum_ -= stack.pop()
                    sum_ -= stack.pop()
                    curr_idx += 1
                elif sum_ > target:
                    sum_ -= stack.pop()
                    sum_ -= stack.pop()
                    curr_idx += 1

        return result


class SolutionX1:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        stack = []
        candidates.sort()
        result = []

        for i, num in enumerate(candidates):

            stack.append(num)
            target -= num
            curr_idx = i
            if target == 0:
                print('hit terminate')
                result.append(stack[:])
                break

            while stack and curr_idx < len(candidates):

                # 如果候选超出索引，则出栈并重置候选
                # if curr_idx == len(candidates):
                #     target += stack.pop()
                #     curr_idx = i + 1
                #     print(candidates[curr_idx], target, stack)
                #     continue

                stack.append(candidates[curr_idx])
                target -= candidates[curr_idx]
                # 仍未满足目标条件
                if target > 0:
                    continue
                    # if target < candidates[i]:
                    #     target += stack.pop()
                    #     curr_idx += 1
                    # else:
                    #     continue
                # 超过目标条件，出栈
                elif target < 0:
                    # 第一次出栈 - 恢复为target > 0的状态
                    target += stack.pop()
                    if target < candidates[curr_idx]:
                        curr_idx += 1
                    # 第二次出栈 - 后续数的操作肯定仍会超过目标，再次出栈能保证与target的距离更远
                    target += stack.pop()
                # 满足目标条件
                else:
                    # 添加子结果
                    print('pop result', stack)
                    result.append(stack[:])
                    while stack[-1] != candidates[i]:
                        target += stack.pop()
                    #
                    print('hi', stack)
                    curr_idx += 1

        return result


def main():
    # candidates = [2, 4, 6, 8]
    # target = 8

    candidates = [2, 3, 6, 7]
    target = 7

    candidates = [2, 3, 5]
    target = 8

    solution = Solution()
    result = solution.combinationSum(candidates, target)
    print(result)


if __name__ == '__main__':
    main()
