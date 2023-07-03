from typing import List
from random import randint

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if sum(nums) < target:
            return 0
        if len(nums) == 1:
            return 1
        res = 100001
        left = 0
        right = 0
        sum_sub_string = 0
        while right < len(nums):
            sum_sub_string += nums[right]
            while sum_sub_string >= target:
                res = min(res, right - left + 1)
                sum_sub_string -= nums[left]
                left += 1
                # print(res, right, left)
            right += 1

        return res


if __name__ == '__main__':
    sol = Solution()
    target = 7
    nums = [2,3,1,2,4,3]
    # target = randint(1, int(1e5))
    # nums = [randint(1, int(1e4)) for _ in range(1000)]
    print(target)
    print(nums)
    print(sol.minSubArrayLen(target, nums))