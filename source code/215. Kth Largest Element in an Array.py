'''
quick_select = half of quick_sort
if k is in the previous part, no need to sort the last part
'''

from typing import List
import random

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return self.quick_select(nums, 0, len(nums)-1, k-1)

    def quick_select(self, nums, start, end, k):
        if start > end:
            return nums[start]
        left = start
        right  = end
        pivot = nums[left]
        while left < right:
            while left < right and nums[right] <= pivot:
                right -= 1
            nums[left] = nums[right]

           
            while left < right and nums[left] >= pivot:
                left += 1
            nums[right] = nums[left]
            
        nums[left] = pivot
        # print(nums[start:end+1], k)
        # print(nums)
        # breakpoint()
        if left == k:
            return nums[left]
        elif left < k:
            return self.quick_select(nums, left+1, end, k)
        else:
            return self.quick_select(nums, start, left-1, k)
       

if __name__ == '__main__':
    sol = Solution()
    orig_nums = [3,2,3,1,2,4,5,5,6]
    # orig_nums = [random.randint(-100, 100) for _ in range(1000)]
    print(orig_nums)
    print(sol.findKthLargest(orig_nums, 4))
    # print(nums)
    for k in range(1, len(orig_nums)+1):
        nums = orig_nums.copy()
        # print(nums)
        print(k, sol.findKthLargest(nums, k))