'''
O(n)
'''


from typing import List
from random import randint
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        left = 0
        right = len(nums) - 1
        res = []

        min_abs_num, min_idx = 10e4, 0
        for idx, num in enumerate(nums):
            # print(abs(num), min_abs_num)
            if abs(num) < min_abs_num:
                min_abs_num = abs(num)
                min_idx = idx
        if min_idx == 0:
            return list(map(lambda x: x**2, nums))
        if min_idx == len(nums) - 1:
            return list(map(lambda x: x**2, nums))[::-1]

        left = min_idx - 1
        right = min_idx + 1
        res = [nums[min_idx] ** 2]


        while left >= 0 or right < len(nums):
            if left >= 0 and right < len(nums):
                if abs(nums[left]) < abs(nums[right]):
                    res.append(nums[left] ** 2)
                    left -= 1
                else:
                    res.append(nums[right] ** 2)
                    right += 1
            elif right < len(nums):
                res.append(nums[right] ** 2)
                right += 1
            else:
                res.append(nums[left] ** 2)
                left -= 1
            # print(left, right, res)
        return res


if __name__ == '__main__':
    sol = Solution()
    nums = [-5, -3, -2, -1]
    # nums = [randint(int(-1e4), int(1e4)) for _ in range(1000)]
    # nums = sorted(nums)
    print(nums)
    print(sol.sortedSquares(nums))