class Solution:
    def totalNQueens(self, n: int) -> int:
        def n_queen_dfs(res, xy_diff, xy_sum, total, n):
            y_loc = len(res)
            if y_loc == n:
                return total + 1

            for x_loc in range(0, n):
                if x_loc not in res and x_loc - y_loc not in xy_diff \
                        and x_loc + y_loc not in xy_sum:
                    total = n_queen_dfs(res + [x_loc],
                                xy_diff + [x_loc - y_loc],
                                xy_sum + [x_loc + y_loc],
                                total,
                                n)
            return total
        total = n_queen_dfs([], [], [], 0, n)
        return total

if __name__ == '__main__':
    s = Solution()
    n = 8
    print(s.totalNQueens(n))