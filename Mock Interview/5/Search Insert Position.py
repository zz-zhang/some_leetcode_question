'''
Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.
'''

class Solution:
    def searchInsert(self, nums, target):
        if target < nums[0]:
            return 0
        if target > nums[-1]:
            return len(nums)

        start = 0
        end = len(nums) - 1
        current = int((start + end) / 2)

        while start <= end:
            if nums[current] == target:
                return current
            if nums[current] > target:
                end = current
                current = int((start + end) / 2)
                if current == end:
                    return current
            if nums[current] < target:
                start = current
                current = int((start + end) / 2)
                if current == start:
                    return current + 1

if __name__ == '__main__':
    sol = Solution()
    nums = [1]
    target = 1
    print(sol.searchInsert(nums, target))

        