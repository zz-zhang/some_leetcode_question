from typing import List
from random import randint
class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        '''
            O(n) solution
        '''
        if len(nums) == 1:
            return 1
        left, right = 0, 1
        # route = [nums[0]]
        res = 1
        while left <= right < len(nums):
            if right < len(nums) and nums[left] < nums[right]:
                while right + 1 < len(nums) and nums[right + 1] >= nums[right]:
                    right += 1
                # route.append(nums[right])
                res += 1
            elif right < len(nums) and nums[left] > nums[right]:
                while right + 1 < len(nums) and nums[right + 1] <= nums[right]:
                    right += 1
                # route.append(nums[right])
                res += 1
            left = right
            right += 1
        # print(route)
        return res


if __name__ == '__main__':
    sol = Solution()
    nums = [1,2,2,3,4,2,2,1]
    
    nums = [randint(0, 1000) for _ in range(1000)]
    print(nums)
    print(sol.wiggleMaxLength(nums))