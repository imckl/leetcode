
# 颠倒给定的 32 位无符号整数的二进制位。
# https://leetcode-cn.com/problems/reverse-bits/
todo

class Solution2:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        oribin='{0:032b}'.format(n)
        print('n', n)
        print('oribin', oribin)
        reversebin=oribin[::-1]
        return int(reversebin,2)


class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        return int(str(n)[::-1], 2)
        # return int(bin(n)[::-1][:-2], 2)


def main():
    n = 10100101000001111010011100
    s = Solution()
    print(s.reverseBits(n))
    s2 = Solution2()
    print(s2.reverseBits(n))


if __name__ == '__main__':
    main()
