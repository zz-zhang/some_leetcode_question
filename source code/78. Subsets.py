class Solution:
    result = []
    def find_subsets(self, nums, s_index, length, sub_res):
        if length == 0:
            self.result.append([_ for _ in sub_res])
            return
        for index in range(s_index, len(nums)):
            sub_res.append(nums[index])
            self.find_subsets(nums, index + 1, length - 1, sub_res)
            sub_res.pop(-1)


    def subsets(self, nums):
        self.result = []
        if len(nums) == 0:
            return [[]]

        for length in range(0, len(nums) + 1):
            self.find_subsets(nums, 0, length, [])
        # print(self.result)
        return self.result

if __name__ == '__main__':
    sol = Solution()
    nums = [0]
    print(sol.subsets(nums))
