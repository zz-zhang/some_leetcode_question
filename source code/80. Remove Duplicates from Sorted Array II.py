from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        prev_num = nums[0]
        prev_count = 1
        total_len = len(nums)
        idx = 1
        while idx < total_len:
            # print(total_len, idx, nums)
            # breakpoint()
            if nums[idx] == prev_num:
                if prev_count == 2:
                    self.shift_list(nums, idx)
                    total_len -= 1
                else:
                    prev_count += 1
                    idx += 1
            else:
                prev_num = nums[idx]
                prev_count = 1
                idx += 1
        return total_len


    def shift_list(self, nums, index):
        temp = nums[index]
        while index < len(nums) - 1:
            nums[index] = nums[index + 1]
            index += 1
        nums[-1] = temp

if __name__ == '__main__':
    sol = Solution()
    nums = [0,0,1,1,1,1,2,3,3]
    print(sol.removeDuplicates(nums), nums)