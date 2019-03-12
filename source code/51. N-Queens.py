class Solution:
    final_res = []


    def forbidden(self, res, y_loc, x_loc):
        for i in range(0, len(res)):
            if x_loc == res[i]:
                return True
            if x_loc - y_loc == res[i] - i:
                return True
            if x_loc + y_loc == res[i] + i:
                return True
        return False

    def find_doable_loc(self, y_loc, n, last_res):
        import copy
        res = copy.deepcopy(last_res)
        for x_loc in range(0, n):
            if not self.forbidden(last_res, y_loc, x_loc):
                loc = x_loc
                res.append(loc)
                if y_loc == n - 1:
                    self.final_res.append(res)
                else:
                    self.find_doable_loc(y_loc + 1, n, res)
                    res.pop(-1)
        # return res


    def res_to_map(self, res, n):
        game_map = []
        for i in range(0, n):
            game_line = '.' * res[i] + 'Q' + '.' * (n - res[i] - 1)
            game_map.append(game_line)
        return game_map


    def solveNQueens(self, n):
        # print(game_map)
        self.find_doable_loc(0, n, [])
        # print(len(self.final_res))
        res_map = []
        for res in self.final_res:
            res_map.append(self.res_to_map(res, n))
        return res_map

    def __init__(self):
        self.final_res = []

if __name__ == '__main__':
    s = Solution()
    n = 2
    print(s.solveNQueens(n))