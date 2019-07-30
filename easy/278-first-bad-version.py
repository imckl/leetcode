# You are a product manager and currently leading a team to develop a new product. Unfortunately, the latest version of
# your product fails the quality check. Since each version is developed based on the previous version, all the versions
# after a bad version are also bad.
# Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one, which causes all the following
# ones to be bad.
# You are given an API bool isBadVersion(version) which will return whether version is bad. Implement a function to
# find the first bad version. You should minimize the number of calls to the API.
# https://leetcode.com/problems/first-bad-version/


# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
def isBadVersion(version: int) -> bool:
    if version >= 5:
        return True
    return False


# 参考了[@liweiwei1419](https://leetcode-cn.com/u/liweiwei1419)分享的[二分法模板](https://leetcode-cn.com/problems/search-insert-position/solution/te-bie-hao-yong-de-er-fen-cha-fa-fa-mo-ban-python-/)：
# https://leetcode-cn.com/problems/search-insert-position/solution/te-bie-hao-yong-de-er-fen-cha-fa-fa-mo-ban-python-/
# 1. 为保证二分法的统一性，这里起始下标为零；因此，实际版本号为索引加一
# 2. 二分法中判断排除的关键：如果中位数不包含坏版本，则起始坏版本一定在中位数之后；这个判断比较好理解，同事排除了中位数，契合模板的要求
# 3. 补充了一些个人的说明，希望能够更易结合分享的模板去理解
class Solution(object):
    def firstBadVersion(self, n: int) -> int:
        # 保证二分法的统一性，这里起始下标为零
        left, right = 0, n - 1

        while left < right:
            # 根据下面的排除条件，左边界排除了中位数，因此选择左中位数
            mid = (left + right) >> 1
            # 如果中位数不包含坏版本，则起始坏版本一定在中位数之后
            # 因为起始下标为零，所以实际版本号为中位数加一
            if not isBadVersion(mid + 1):
                left = mid + 1
            # 否则，起始坏版本可能是中位数，或者中位数之前（注意这里并不能排除中位数）
            else:
                right = mid

        # 返回的结果一定是版本号之一，所以不用做是否版本号的判断
        # 实际版本号为索引加一
        return left + 1


def main():
    n = 7
    solution = Solution()
    result = solution.firstBadVersion(n)
    print(result)


if __name__ == '__main__':
    main()
