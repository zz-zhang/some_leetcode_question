#not finished
class Solution:
    def inOrder(self, nums):
        i = 1
        while i < len(nums):
            if nums[i] > nums[i - 1]:
                return False
            i += 1
        return True

    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if self.inOrder(nums):
            nums.sort()
            # return nums

        for i in range(len(nums) - 1, 0, -1):
            max = 0
            flag = 0
            for j in range(i - 1, 0, -1):
                if nums[j] < nums[i]:
                    if nums[j] < max:
                        max = nums[j]
                        flag = j
            if flag != 0:
                nums[i] = nums[i] + nums[flag]
                nums[flag] = nums[i] - nums[flag]
                nums[i] = nums[i] - nums[flag]
                # nums1 = nums[0 : i + 1]
                # nums2 = sorted(nums[i+1:])
                # nums = nums1 + nums2
                break
        return nums

if __name__ == '__main__':
    sol = Solution()
    nums = [1, 3, 2]
    print(sol.nextPermutation(nums))