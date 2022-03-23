from typing import *

class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        dp = [0 for _ in range(len(nums))]
        dp[0] = nums[0]
        max_prev = dp[0]
        max_prev_idx = 0

        for idx, num in enumerate(nums[1:]):
            # breakpoint()
            # print(idx + 1, max_prev_idx, '-')
            if (idx + 1) - max_prev_idx > k:
                max_prev = -10 ** 9
                for bias in range(1, k + 1):
                    # print(idx + 1 - bias, dp[idx + 1 - bias])
                    if idx + 1 - bias >= 0:
                        if dp[idx + 1 - bias] > max_prev:
                            max_prev = dp[idx + 1 - bias]
                            max_prev_idx = idx + 1 - bias
                    else:
                        break
            else:
                if dp[(idx + 1) - 1] > max_prev:
                    max_prev = dp[(idx + 1) - 1]
                    max_prev_idx = (idx + 1) - 1
            dp[idx + 1] = num + max_prev
        # print(dp)
        return dp[-1]

if __name__ == '__main__':
    sol = Solution()
    nums = [1,-5,-20,4,-1,3,-6,-3]
    k = 2
    sol.maxResult(nums, k)