class Solution:
    def access(self, nums, accessed, item, length):
        if item - 1 in nums:
            smaller = nums.index(item - 1)
            if not accessed[smaller]:
                accessed[smaller] = True
                length = self.access(nums, accessed, item - 1, length + 1)
        if item + 1 in nums:
            larger = nums.index(item + 1)
            if larger != -1 and not accessed[larger]:
                accessed[larger] = True
                length = self.access(nums, accessed, item + 1, length + 1)
        return length


    def longestConsecutive(self, nums) -> int:
        accessed = [False for item in nums]
        res = 0
        for index in range(0, len(nums)):
            if not accessed[index]:
                accessed[index] = True
                length = self.access(nums, accessed, nums[index], 1)
                res = max(res, length)
        return res

if __name__ == '__main__':
    sol = Solution()
    nums = [100, 4, 200, 1, 3,2]
    print(sol.longestConsecutive(nums))
