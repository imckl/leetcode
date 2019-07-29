
# 编写一个算法来判断一个数是不是“快乐数”。
#
# 一个“快乐数”定义为：对于一个正整数，每一次将该数替换为它每个位置上的数字的平方和，然后重复这个过程直到这个数变为 1，也可能是无限循环但始终变不到 1。如果可以变为 1，那么这个数就是快乐数。
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/happy-number
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。


class Solution(object):
    def isHappy(self, n: int) -> bool:
        sum_digit_power = lambda n: sum(int(i) ** 2 for i in str(n))
        result_set = set()

        while n != 1:
            n = sum_digit_power(n)
            if n not in result_set:
                result_set.add(n)
            else:
                return False

        return True


class Solution2(object):
    def isHappy(self, n: int) -> bool:
        sum_digit_power = lambda n: sum(int(i) ** 2 for i in str(n))
        result_dict = {}

        while True:
            n = sum_digit_power(n)
            if n == 1:
                return True
            elif result_dict.get(n):
                return False
            result_dict[n] = 1


def main():
    n = 19
    solution = Solution()
    result = solution.isHappy(n)
    print(result)


if __name__ == '__main__':
    main()
