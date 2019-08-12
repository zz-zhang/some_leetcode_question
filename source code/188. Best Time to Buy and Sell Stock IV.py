class Solution:
    def maxProfit(self, k, prices):
        result = 0
        while len(prices) > 0:

            buy_price = [prices[0]]
            buy_index = [0]
            sell_price = [prices[-1]]
            sell_index = [len(prices) - 1]

            for i in range(1, len(prices)):
                buy_price.append(min(buy_price[i - 1], prices[i]))
                if buy_price[i] == prices[i]:
                    buy_index.append(i)
                else:
                    buy_index.append(buy_index[i - 1])

                sell_price.append(max(sell_price[i - 1], prices[len(prices) - i - 1]))
                if sell_price[i] == prices[len(prices) - i - 1]:
                    sell_index .append(len(prices) - i - 1)
                else:
                    sell_index.append(sell_index[i - 1])

            sell_price = sell_price[::-1]
            sell_index = sell_index[::-1]

            trade = [(sell_price[i] - buy_price[i], buy_index[i], sell_index[i]) for i in range(0, len(prices))]
            trade = sorted(trade, key=lambda x:(x[0], x[1], x[2]), reverse=True)

            result += trade[0][0]
            buy_forbid = trade[0][1]
            sell_forbid = trade[0][2]
            k -= 1
            if k == 0:
                break
            prices.pop(sell_forbid)
            prices.pop(buy_forbid)

            # print(trade)

            # buy_forbid = []
            # sell_forbid = []
            # for i in range(0, len(prices)):
            #     if trade[i][1] not in buy_forbid and trade[i][2] not in sell_forbid:
            #         buy_forbid.append(trade[i][1])
            #         sell_forbid.append(trade[i][2])
            #         result += trade[i][0]
            #         k -= 1
            #     if k == 0:
            #         break

        return result


if __name__ == '__main__':
    sol = Solution()
    input_array = [6,1,3,2,4,7]
    k = 2
    print(sol.maxProfit(k, input_array))
