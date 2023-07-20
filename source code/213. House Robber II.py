from typing import List
import random

class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        dp_select_0 = [0 for _ in range(len(nums) + 1)]
        dp_not_select_0 = [0 for _ in range(len(nums) + 1)]
        dp_select_0[1] = nums[0]
        dp_select_0[2] = nums[0]
        dp_not_select_0[2] = nums[1]
        # print(dp_select_0)
        # print(dp_not_select_0)
        # print('___')

        for idx, num in enumerate(nums[2:]):
            idx += 3
            if idx == len(nums):
                dp_not_select_0[idx] = num
                dp_not_select_0[idx] = max(dp_not_select_0[idx-1], dp_not_select_0[idx-2] + num)

                dp_select_0[idx] = dp_select_0[idx - 1]
            else:
                if idx - 2 < 0:
                    dp_select_0[idx] = num
                    # dp_not_select_0[idx] = num
                else:
                    dp_select_0[idx] = max(dp_select_0[idx-1], dp_select_0[idx-2] + num)
                    dp_not_select_0[idx] = max(dp_not_select_0[idx-1], dp_not_select_0[idx-2] + num)
            # print(dp_select_0)
            # print(dp_not_select_0)
            # print('___')
        return max(dp_select_0[-1], dp_not_select_0[-1])

if __name__ == '__main__':
    sol = Solution()
    nums = [2,3]
    # nums = [random.randint(0, 1000) for _ in range(100)]
    print(nums)
    print(sol.rob(nums))