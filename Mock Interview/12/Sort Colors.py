from random import randint


class Solution:
    def sortColors(self, nums):
        current = 3
        index = -1
        for idx, color in enumerate(nums):
            if color < current:
                current = color
                index = idx
        
        nums[0], nums[index] = nums[index], nums[0]
        if current not in nums[1:]:
            current += 1
        # print(nums)
        i = 1
        while i < len(nums):
            if nums[i] != current:
                j = i + 1
                while j < len(nums):
                    if nums[j] == current:
                        nums[i], nums[j] = nums[j], nums[i]
                        break
                    j += 1
            if current not in nums[i+1:]:
                current += 1
            # print(nums, current)
            # breakpoint()
            i += 1
        
if __name__ == '__main__':
    sol = Solution()
    nums = [randint(0,2) for _ in range(300)]
    sol.sortColors(nums)
    print(nums)