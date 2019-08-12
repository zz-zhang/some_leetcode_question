class Solution:
    # binary search with some condition

    def binary_search(self, nums, target, start, end, bias):
        if start > end:
            return -1
        index = int((start + end) / 2)
        if nums[index] == target:
            if 0 <= (index + bias)< len(nums) and nums[index + bias] != target:
                return index
            elif bias < 0:
                return self.binary_search(nums, target, start, index - 1, bias)
            else:
                return self.binary_search(nums, target, index + 1, end, bias)
        elif nums[index] < target:
            return self.binary_search(nums, target, index + 1, end, bias)
        else:
            return self.binary_search(nums, target, start, index - 1, bias)

    # def binary_search_sinary(self, nums, target, start, end, bias):


    def searchRange(self, nums, target):
        if len(nums) == 0:
            return [-1, -1]
        nums = [nums[0] - 0x0fffffff] + nums + [nums[len(nums) - 1] + 0x0fffffff]
        # print(nums)
        start_index = self.binary_search(nums, target, 0, len(nums) - 1, -1)
        if start_index == -1:
            return [-1, -1]
        else:
            start_index -= 1
            end_index = self.binary_search(nums, target, 0, len(nums) - 1, 1) - 1
            # print(start_index, end_index)
            return [start_index, end_index]


if __name__ == '__main__':
    sol = Solution()
    nums = [2,2]
    target = 3
    print(sol.searchRange(nums, target))
