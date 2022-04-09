from random import randint
from typing import List
from random import choice

class Solution:

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import defaultdict
        counter = defaultdict(int)
        for num in nums:
            counter[num] += 1
        # print(counter)
        res = [(num, count) for num, count in counter.items()]
        res = sorted(res, key=lambda x: x[1], reverse=True)
        res = [num for num, count in res[:k]]
        return res


if __name__ == '__main__':
    sol = Solution()
    nums = [1]
    k = 1
    sol.topKFrequent(nums, k)