# 给定一个数组，它的第 i 个元素是一支给定股票第 i 天的价格。
#
# 设计一个算法来计算你所能获取的最大利润。你可以尽可能地完成更多的交易（多次买卖一支股票）。
#
# 注意：你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-ii
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit_sum = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i - 1]:
                max_profit_sum += prices[i] - prices[i - 1]
        return max_profit_sum


class Solution5:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0

        max_profit_sum = 0
        min_price = prices[0]
        max_profit = 0

        for i in range(1, len(prices)):
            if prices[i] < min_price:
                min_price = prices[i]
            else:
                cur_profit = prices[i] - min_price
                # 当天价格高于明天的价格，则当天价格为最高价
                # 并设置最低价为后天的价格
                try:
                    if prices[i] > prices[i + 1]:
                        max_profit = cur_profit
                        max_profit_sum += max_profit
                        min_price = prices[i + 1]
                        max_profit = 0
                except IndexError:
                    max_profit = cur_profit
                # 当前利润大于最大利润，则最大利润为当前利润
                if cur_profit > max_profit:
                    max_profit = cur_profit

        return max_profit_sum + max_profit


class Solution4:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0

        max_profit_list = []
        min_price = prices[0]

        while prices:
            for i in range(len(prices)):
                if prices[i] <= min_price:
                    min_price = prices[i]
                    prices.pop(0)
                    break
                else:
                    try:
                        if prices[i] > prices[i + 1]:
                            max_profit_list.append(prices[i] - min_price)
                            prices[:] = prices[i + 1:]
                            min_price = prices[0]
                            break
                    except IndexError:
                        max_profit_list.append(prices[i] - min_price)
                        prices = []

        return sum(max_profit_list)


class Solution3:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        min_price = prices[0]
        max_profit = 0
        max_profit_list = []

        self._max_profit_partial(prices, max_profit_list)
        print(max_profit_list)
        return sum(filter(lambda n: n is not None, max_profit_list))

    def _max_profit_partial(self, prices: List[int], max_profit_list: List[int]):
        if not prices:
            return
        min_price = prices[0]
        max_profit = 0
        for i, price in enumerate(prices[1:], 1):
            if price < min_price:
                min_price = price
            else:
                if i == len(prices) - 1:
                    max_profit = price - min_price
                    max_profit_list.append(max_profit)
                    return
                else:
                    print(price, prices[i + 1])
                    if price > prices[i + 1]:
                        max_profit = price - min_price
                        max_profit_list.append(max_profit)
                        # print(max_profit_list)
                        max_profit_list.append(self._max_profit_partial(prices[i + 1:], max_profit_list))


class Solution2:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        min_price = prices[0]
        max_profit = 0
        for i, price in enumerate(prices[1:]):
            if price < min_price:
                min_price = price
            else:
                if price - min_price > max_profit:
                    max_profit = price - min_price
                return max_profit + self.maxProfit(prices[i + 1:])
        return max_profit


if __name__ == '__main__':
    # prices = [7, 1, 5, 3, 6, 4]
    # prices = [7, 6, 4, 3, 1]
    # prices = [1, 2, 4, 11, 7]
    # prices = [1, 2, 3, 4, 5]
    prices_ = [2, 1, 2, 0, 1]
    s = Solution()
    r = s.maxProfit(prices_)
    print(r)
