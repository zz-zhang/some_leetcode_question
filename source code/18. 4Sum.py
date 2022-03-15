# class Solution:
    # def fourSum(self, nums, target):
    #     nums = self.quick_sort(nums, 0, len(nums) - 1)
    #     res = []
    #     q = [(0,len(nums) - 1)]
    #     while len(q) > 0:
    #         # print(q)
    #         i, j = q[0]
    #         new_tgt = target - nums[i] - nums[j]
    #         able, (res1, res2) = self.two_sum(nums[i + 1: j], new_tgt)
    #         if able:
    #             res = res + [nums[i], nums[j], res1, res2]
    #         else:
    #             if new_tgt + res1 > target and i + 1 < j - 2:
    #                 q.append((i + 1, j))
    #                 continue
    #             if new_tgt + res2 < target and i < j - 2 - 1:
    #                 q.append((i, j - 1))
    #                 continue
                
    #             if i + 1 < j - 2:
    #                 q.append((i + 1, j))
    #             if i < j - 2 - 1:
    #                 q.append((i, j - 1))
    #         q = q[1:]
    #     return res

    # def two_sum(self, nums, target):
    #     i = 0
    #     j = len(nums) - 1
    #     res = []
    #     while i < j:
    #         if nums[i] + nums[j] == target:
    #             return True, (nums[i], nums[j])
    #         elif nums[i] + nums[j] < target:
    #             i += 1
    #         else:
    #             j -= 1
        
    #     return False, (target[0] + target[1], target[-1] + target[-2])

    # def partition(self, nums, left, right):
    #     pivot = nums[left]
    #     i = left
    #     j = right
    #     # print('+++')
    #     # print(nums, pivot)
    #     while i < j:
    #         while i < j and nums[j] >= pivot:
    #             j -= 1
    #         if i < j:
    #             nums[i], nums[j] = nums[j], nums[i]
    #             i += 1
    #         # print(nums)
    #         # breakpoint()
    #         while i < j and nums[i] <= pivot:
    #             i += 1
    #         if i < j:
    #             nums[i], nums[j] = nums[j], nums[i]
    #             j -= 1
    #         # print(nums)
    #     # print(nums)
    #     return i
    
    # def quick_sort(self, nums, left=None, right=None):
    #     left = 0 if left is None else left
    #     right = len(nums) - 1 if left is None else right
    #     if left < right:
    #         partition_idx = self.partition(nums, left, right)
    #         self.quick_sort(nums, left, partition_idx - 1)
    #         self.quick_sort(nums, partition_idx + 1, right)
    #     return nums
        
from random import randint


class Solution:
    def fourSum(self, nums, target):
        nums = self.quick_sort(nums, 0, len(nums) - 1)
        res = []
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                for k in range(j + 1, len(nums)):
                    for l in range(k + 1, len(nums)):
                        arr = [nums[i], nums[j], nums[k], nums[l]]
                        s = sum(arr)
                        # print(arr, s)
                        if s == target and not self.list_exist(res, arr):
                            res.append(arr)
                        if s > target:
                            break
        return res

    def list_exist(self, lst, tgt):
        # breakpoint()
        for l in lst:
            equal = True
            for n1, n2, in zip(l, tgt):
                if n1 != n2:
                    equal = False
                    break
            if equal:
                return True
        return False

    def partition(self, nums, left, right):
        pivot = nums[left]
        i = left
        j = right
        # print('+++')
        # print(nums, pivot)
        while i < j:
            while i < j and nums[j] >= pivot:
                j -= 1
            if i < j:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
            # print(nums)
            # breakpoint()
            while i < j and nums[i] <= pivot:
                i += 1
            if i < j:
                nums[i], nums[j] = nums[j], nums[i]
                j -= 1
            # print(nums)
        # print(nums)
        return i
    
    def quick_sort(self, nums, left=None, right=None):
        left = 0 if left is None else left
        right = len(nums) - 1 if left is None else right
        if left < right:
            partition_idx = self.partition(nums, left, right)
            self.quick_sort(nums, left, partition_idx - 1)
            self.quick_sort(nums, partition_idx + 1, right)
        return nums

if __name__ == '__main__':
    sol = Solution()
    nums = [randint(-1000000000, 1000000000) for _ in range(200)]
    target = randint(-1000000000, 1000000000)
    # nums = [1,0,-1,0,-2,2]
    # target = 0
    print(sol.fourSum(nums, target))