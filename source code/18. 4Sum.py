from random import randint
from typing import List
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums = sorted(nums)

        res = set()
        # breakpoint()
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            for j in range(i + 1, len(nums)):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue

                left, right = j + 1, len(nums) - 1
                while left < right:
                    numbers = (nums[i], nums[j], nums[left], nums[right])
                    s = sum(numbers)
                    print(numbers, s, target)
                    if s == target:
                        res.add(numbers)
                        left += 1
                        right -= 1
                    elif s < target:
                        left += 1
                    else:
                        right -= 1
        return list(res) 



if __name__ == '__main__':
    sol = Solution()
    nums = [randint(-1000000000, 1000000000) for _ in range(200)]
    target = randint(-1000000000, 1000000000)
    nums = [-3,-2,-1,0,0,1,2,3]
    target = 0
    print(sol.fourSum(nums, target))