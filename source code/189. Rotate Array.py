from typing import List

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        k = k % len(nums)
        recoder = []
        idx = 0

        for idx, num in enumerate(nums):
            new_idx = (idx + k) % len(nums)
            recoder.append((new_idx, num))
        # print(queue)

        for idx, val in recoder:
            nums[idx] = val

if __name__ == '__main__':
    sol = Solution()
    nums = [1,2,3,4]
    k = 2
    sol.rotate(nums, k)
    print(nums)