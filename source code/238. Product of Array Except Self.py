from typing import List
from random import randint
import operator
from functools import reduce

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # w/o using division operation
        zero_num = nums.count(0)

        if zero_num >= 2:
            return [0] * len(nums)

        if zero_num == 1:
            zero_idx = nums.index(0)
            product = reduce(operator.mul, [num for idx, num in enumerate(nums) if idx != zero_idx])
            res = [0] * len(nums)
            res[zero_idx] = product
            return res
        
        prefix = [1]
        surfix = [1]
        for idx, num in enumerate(nums):
            prefix.append(prefix[-1] * num)
            surfix.append(surfix[-1] * nums[len(nums) - 1 - idx])
        prefix.pop(-1)
        surfix.pop(-1)
        surfix.reverse()
        
        res = [p * f for p, f in zip(prefix, surfix)]
        return res
    


if __name__ == '__main__':
    sol = Solution()
    nums = [1, 2, 3, 4]
    nums = [randint(-30, 30) for _ in range(10)]
    print(nums)
    print(sol.productExceptSelf(nums))