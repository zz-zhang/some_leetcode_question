from typing import List
from random import choice
from pprint import pprint

class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:

        current_sta = [i for i in range(len(grid[0]))]
        last_col = len(current_sta) - 1
        for r_idx, row in enumerate(grid):
            next_sta = [-1 for _ in current_sta]
            for b_idx, loc in enumerate(current_sta):
                if loc == -1:
                    next_sta[b_idx] = -1
                else:
                    if row[loc] == 1:
                        if loc == last_col:
                            next_sta[b_idx] = -1
                        elif row[loc + 1] == -1:
                            next_sta[b_idx] = -1
                        else:
                            next_sta[b_idx] = loc + 1
                    else:
                        if loc == 0:
                            next_sta[b_idx] = -1
                        elif row[loc - 1] == 1:
                            next_sta[b_idx] = -1
                        else:
                            next_sta[b_idx] = loc - 1
            # print(r_idx, next_sta)
            current_sta = [i for i in next_sta]
        # print(next_sta)
        return next_sta



if __name__ == '__main__':
    sol = Solution()
    grid =[[1],[-1],[-1],[-1],[1],[-1],[-1],[1],[1],[1],[1],[1],[-1],[1],[1],[1],[1],[-1],[1],[-1],[1],[-1],[-1],[1],[-1],[1],[-1],[-1],[1],[-1],[-1],[1],[1],[1],[1],[-1],[1],[-1],[-1],[-1],[-1],[-1],[-1],[-1],[1],[1],[-1],[1],[-1],[-1],[-1],[-1],[-1],[-1],[1],[1],[-1],[-1],[1],[1],[1],[-1],[-1],[-1],[-1],[-1],[-1],[-1],[-1],[1],[1],[-1],[1],[-1],[1],[1],[1],[1],[-1],[1],[-1],[1],[1],[1],[-1],[1],[-1],[1],[-1],[1],[1],[-1],[-1],[1],[1],[-1],[1],[-1],[1],[-1]]
    print(sol.findBall(grid))