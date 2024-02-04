from typing import List
from random import randint
from collections import defaultdict
from time import time


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = 0
        prefix_sum = []
        for num in nums:
            if len(prefix_sum) == 0:
                prefix_sum.append(num)
            else:
                prefix_sum.append(num + prefix_sum[-1])

        counter = defaultdict(int)
        for idx in range(len(nums)):
            if prefix_sum[idx] == k:
                res += 1
            if prefix_sum[idx] - k in counter:
                res += counter[prefix_sum[idx] - k]
            counter[prefix_sum[idx]] += 1
        return res


if __name__ == '__main__':
    sol = Solution()
    # nums = [-1,1,1,1]
    # k = 2
    nums = [0 for _ in range(int(2e4))]
    k = 0
    # print(nums)
    start_time = time()
    print(sol.subarraySum(nums, k))
    print(time() - start_time)