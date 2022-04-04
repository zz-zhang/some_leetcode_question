from random import randint
from typing import List


class Solution:

    def splitArray(self, nums: List[int], m: int) -> int:
        if m == len(nums):
            return max(nums)
        res = []
        while m > 1:
            last_start = res[0][0] if len(res) > 0 else 0
            last_end = res[0][1] if len(res) > 0 else len(nums)
            res = res[1:]
            idx_res, sum1, sum2 = self.split(nums[last_start: last_end])
            # print(last_start, idx_res, last_end, sum1, sum2)

            res.append((last_start, idx_res, sum1))
            res.append((idx_res, last_end, sum2))
            res = sorted(res, key=lambda x: x[-1], reverse=True)
            m -= 1
            print(res)
        return res[0][-1]

    def split(self, nums):
        min_res = 10 ** 10
        idx_res = 0
        for idx in range(len(nums)):
            sub_min = max(sum(nums[:idx]), sum(nums[idx:]))
            if sub_min < min_res:
                min_res = sub_min
                idx_res = idx
        return idx_res, sum(nums[:idx_res]), sum(nums[idx_res:])

if __name__ == '__main__':
    sol = Solution()
    nums = [50, 21, 28, 39, 22, 2, 87, 98, 59, 33, 24, 30, 42, 94, 72, 95, 55, 36, 97, 43]
    m = 4
    # nums = [randint(0, 100) for _ in range(20)]
    # m = 2
    print(nums)
    print(sol.splitArray(nums, m))
