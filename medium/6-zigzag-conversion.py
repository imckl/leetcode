# The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this:
# (you may want to display this pattern in a fixed font for better legibility)


class Solution(object):
    # 规律：
    # 1. total = (num_rows - 1) * 2
    # 2. second = 2 * (i - 1)
    # 3. first = total - second
    def convert(self, s: str, numRows: int) -> str:
        # 行数为一，则直接返回s
        if numRows == 1:
            return s

        result = ''  # 最终字符串
        length = len(s)

        total = (numRows - 1) * 2

        for i in range(numRows):
            second_step = 2 * i
            first_step = total - second_step

            curr_step = False
            steps = (first_step, second_step,)

            move = i
            pre_move = -1
            while move < length:
                if move != pre_move:
                    result += s[move]
                pre_move = move
                move += steps[curr_step]
                curr_step = not curr_step

        return result
