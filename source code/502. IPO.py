from typing import List
import heapq


class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int],
                             capital: List[int]) -> int:
        res = w
        pairs = [(prof, cond) for prof, cond in zip(profits, capital)]
        pairs = sorted(pairs, key=lambda x: x[1])
        last_idx = 0
        heap = []
        while k > 0:
            new_idx = last_idx
            for i in range(new_idx, len(pairs)):
                if pairs[i][1] > res:
                    new_idx = i
                    break
            else:
                new_idx = len(pairs)

            for prof, _ in pairs[last_idx:new_idx]:
                heapq.heappush(heap, prof * -1)
            # print(heap)

            if len(heap) == 0:
                profit = 0
            else:
                profit = heapq.heappop(heap) * -1

            res += profit
            last_idx = new_idx
            k -= 1

        return res


if __name__ == '__main__':
    sol = Solution()
    k = 2
    w = 10
    profits = [1, 2, 3]
    capital = [1, 1, 1]

    # k = 100000
    # w = 100000000
    # profits = [random.randint(0, 10000) for _ in range(100000)]
    # capital = [random.randint(0, 1000000000) for _ in range(100000)]
    # print(k)
    print(sol.findMaximizedCapital(k, w, profits, capital))