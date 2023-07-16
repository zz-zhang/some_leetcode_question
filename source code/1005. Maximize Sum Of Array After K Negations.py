from typing import List
from random import randint
class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        nums = sorted(nums)
        positive = [True if n >= 0 else False for n in nums]

        if all(positive):
            k = k % 2
            if k == 1:
                min_pos = min(nums)
                return sum(nums) - min_pos * 2
            else:
                return sum(nums)

        num_neg = positive.count(False)
        if k >= num_neg:
            k -= num_neg
            nums = [abs(n) for n in nums]
            k = k % 2
            if k == 1:
                min_pos = min(nums)
                return sum(nums) - min_pos * 2
            else:
                return sum(nums)
        else:
            for idx in range(k):
                nums[idx] = -nums[idx]
            return sum(nums)


if __name__ == '__main__':
    sol = Solution()
    nums  = [2,-3,-1,5,-4]
    k = 4
    nums = [randint(-100, 100) for _ in range(10000)]
    print(nums)
    print(sol.largestSumAfterKNegations(nums, k))