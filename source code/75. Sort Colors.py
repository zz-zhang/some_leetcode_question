class Solution:
    def sortColors(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        counter = [0, 0, 0]
        for i in nums:
            counter[i] += 1
        for index in range(0, len(nums)):
            if 0 <= index < counter[0]:
                nums[index] = 0
            elif index < counter[0] + counter[1]:
                nums[index] = 1
            else:
                nums[index] = 2


if __name__ == '__main__':
    sol = Solution()
    nums = []
    sol.sortColors(nums)
    print(nums)
