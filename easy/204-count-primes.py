
# 统计所有小于非负整数 n 的质数的数量。
# https://leetcode-cn.com/problems/count-primes/

import math


class Solution(object):
    def countPrimes(self, n: int) -> int:
        if n < 2:
            return 0

        primes = [True] * n

        primes[0] = False
        primes[1] = False

        for i in range(2, int(n ** 0.5) + 1):
            if primes[i]:
                # for j in range(i * i, n, i):
                #     primes[j] = False
                primes[i * i:n:i] = [False] * len(primes[i * i: n: i])

        return len(list(filter(lambda n: n == True, primes)))


class Solution3(object):
    def countPrimes(self, n: int) -> int:
        if n < 2:
            return 0

        nums = [i for i in range(2, n)]
        result = []

        i = 0
        while nums:
            # print(nums)
            m = nums[0]
            k = 2
            while m * k < n:
                if m * k in nums:
                    nums.remove(m * k)
                k += 1
            result.append(nums.pop(0))

        return len(result)
        # print(result)



class Solution2(object):
    def countPrimes(self, n: int) -> int:
        count = 0
        for i in range(1, n):
            if self._is_prime(i):
                count += 1
        return count

    def _is_prime(self, n: int) -> bool:
        if n == 1:
            return False
        for i in range(2, int(math.sqrt(n) + 1)):
            if n % i == 0:
                return False
        return True


def main():
    n = 5000000
    solution = Solution()
    result = solution.countPrimes(n)
    print(result)


if __name__ == '__main__':
    main()
