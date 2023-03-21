from typing import List

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
        if rowIndex == 1:
            return [1, 1]
        last = [1, 1]
        for row in range(1, rowIndex+1):
            res = [1]
            for col in range(1, row):
                res.append(last[col-1] + last[col])
            res.append(1)
            last = res
        return res

if __name__ == '__main__':
    sol = Solution()
    rowIndex = 3
    print(sol.getRow(rowIndex))