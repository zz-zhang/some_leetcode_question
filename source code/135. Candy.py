from typing import List
from random import randint

class Solution:
    def candy(self, ratings: List[int]) -> int:
        candies = [1]
        min_candy = candies[0]

        for r1, r2 in zip(ratings[:-1], ratings[1:]):
            if r2 > r1:
                candies.append(candies[-1]+1)
            else:
                candies.append(1)
        # print(candies)

        for idx_r in range(len(candies) - 1, 0, -1):
            idx_l = idx_r - 1
            left = ratings[idx_l]
            right = ratings[idx_r]
            if left > right:
                candies[idx_l] = max(candies[idx_l], candies[idx_r] + 1)
        # print(candies)
        return sum(candies)

if __name__ == '__main__':
    sol = Solution()
    ratings = [5,4,3,2,3,4,1]
    ratings = [randint(0, 20000) for _ in range(20000)]
    print(ratings)
    print(sol.candy(ratings))