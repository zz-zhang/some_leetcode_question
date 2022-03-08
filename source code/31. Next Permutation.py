#not finished
class Solution:

    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        is_order, index = self._in_order(nums)
        if is_order:
            nums = nums[::-1]
            # print(nums)
        else:
            nums[index] += nums[index + 1]
            nums[index + 1] = nums[index] - nums[index + 1]
            nums[index] = nums[index] - nums[index + 1]

    def _in_order(self, nums):
        for i in range(len(nums) - 1):
            print(nums[i + 1], nums[i])
            if nums[i + 1] > nums[i]:
                return False, i
        return True, 0

if __name__ == '__main__':
    sol = Solution()
    nums = [1, 3, 2]
    sol.nextPermutation(nums)
    print(nums)