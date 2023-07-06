from typing import List
from random import randint
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        src, tgt = 0, 0
        while src < len(nums):
            if nums[src] != val:
                nums[tgt] = nums[src]
                tgt += 1
            src += 1

        # print(nums, src, tgt)
        return tgt

if __name__ == '__main__':
    sol = Solution()
    nums = [0, 0, 1]
    val = 0
    # nums = [randint(0, 50) for _ in range(100)]
    # val = nums[0]
    print(nums, val)
    print(sol.removeElement(nums, val))
    print(nums)