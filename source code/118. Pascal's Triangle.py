from typing import List

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 1:
            return [[1]]
        if numRows == 2:
            return [[1], [1, 1]]
        res = [[1], [1, 1]]
        for row in range(2, numRows):
            sub_res = [1]
            for col in range(1, row):
                sub_res.append(res[row-1][col-1] + res[row-1][col])
            sub_res.append(1)
            res.append(sub_res)
        return res

if __name__ == '__main__':
    sol = Solution()
    numRows = 5
    print(sol.generate(numRows))