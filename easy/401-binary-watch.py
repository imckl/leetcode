# https://leetcode-cn.com/problems/binary-watch/

from typing import List


class Solution(object):

    def __init__(self):
        max_minute = 60
        max_hour = 12

        self._count_result = [[] for _ in range(4 + 6 + 1)]

        for m in range(max_minute):
            for h in range(max_hour):
                bit_count = self._bit_count(m) + self._bit_count(h)
                self._count_result[bit_count].append('{0:d}:{1:02d}'.format(h, m))

    def readBinaryWatch(self, num: int) -> List[str]:
        return self._count_result[num]

    def _bit_count(self, num: int) -> int:
        count = 0
        while num != 0:
            num &= num - 1
            count += 1
        return count


def main():
    solution = Solution()
    for i in solution._count_result:
        print(i)


if __name__ == '__main__':
    main()
