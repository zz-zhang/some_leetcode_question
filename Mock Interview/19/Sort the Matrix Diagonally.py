from tempfile import tempdir
from typing import *
from pprint import pprint

class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        r = len(mat)
        c = len(mat[0])
        i = 0
        temp = []
        temp_idx = []
        while i < r:
            bias = 0
            sub_temp = []
            sub_idx = []
            while i + bias < r and bias < c:
                sub_temp.append((mat[i + bias][bias]))
                sub_idx.append((i + bias, bias))
                bias += 1
            temp.append(sorted(sub_temp))
            temp_idx.append(sub_idx)
            i += 1
        # print(temp)

        i = 0
        while i < c:
            bias = 0
            sub_temp = []
            sub_idx = []
            while bias < r and i + bias < c:
                sub_temp.append((mat[bias][i + bias]))
                sub_idx.append((bias, i + bias))
                bias += 1
            temp.append(sorted(sub_temp))
            temp_idx.append(sub_idx)
            i += 1
        # print(temp)

        for line, coord in zip(temp, temp_idx):
            for val, coor in zip(line, coord):
                i, j = coor
                mat[i][j] = val
        # pprint(mat)
        return mat

if __name__ == '__main__':
    sol = Solution()
    mat = [[11,25,66,1,69,7],[23,55,17,45,15,52],[75,31,36,44,58,8],[22,27,33,25,68,4],[84,28,14,11,5,50]]
    sol.diagonalSort(mat)