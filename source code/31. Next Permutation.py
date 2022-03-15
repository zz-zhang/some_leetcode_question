#not finished
from math import prod


class Solution:

    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        i = len(nums) - 1
        pos = -1
        while i > 0:
            if nums[i] > nums[i - 1]:
                pos = i - 1
                break
            i -= 1

        min_val = 101
        min_idx = -1
        for i in range(len(nums) - 1, pos, -1):
            if nums[i] > nums[pos]:
                if nums[i] < min_val:
                    min_val = nums[i]
                    min_idx = i

        nums[pos], nums[min_idx] = nums[min_idx], nums[pos]

        # keep sub_list after i in increasing order
        self.quick_sort(nums, pos + 1, len(nums) - 1)
        return

    def partional(self, nums, left, right):
        pivot = nums[left]
        i = left
        j = right
        while i < j:
            while i < j and nums[j] >= pivot:
                j -= 1
            nums[i] = nums[j]
            while i < j and nums[i] <= pivot:
                i += 1
            nums[j] = nums[i]
        nums[i] = pivot
        return i

    def quick_sort(self, nums, left=None, right=None):
        if left is None or right is None:
            left = 0
            right = len(nums) - 1
        if left < right:
            pivot_idx = self.partional(nums, left, right)
            self.quick_sort(nums, left, pivot_idx - 1)
            self.quick_sort(nums, pivot_idx + 1, right)


if __name__ == '__main__':
    sol = Solution()
    nums = [5,4,3,2,1]
    # print(prod(range(1, 2)))
    for _ in range(prod(range(1, len(nums) + 1)) + 1):
        sol.nextPermutation(nums)
        print(nums)