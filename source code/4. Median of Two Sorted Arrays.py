class Solution:
    def partition(self, nums, begin, end):
        x = nums[end]
        i = begin - 1
        for j in range(begin, end):
            if nums[j] <= x:
                i += 1
                nums[i], nums[j] = nums[j], nums[i]
        nums[i + 1], nums[end] = nums[end], nums[i + 1]
        return i + 1

    def find_kth_largest_num(self, nums, target, begin, end):
        if begin == end:
            return begin
        index = self.partition(nums, begin, end)
        k = index - begin + 1
        if k == target:
            return index
        elif target < k:
            return self.find_kth_largest_num(nums, target, begin, index - 1)
        else:
            return self.find_kth_largest_num(nums, target - k, index + 1, end)

    def findMedianSortedArrays(self, nums1, nums2):
        nums = nums1 + nums2
        if len(nums) % 2 == 0:
            index = self.find_kth_largest_num(nums, int(len(nums) / 2) + 1, 0, len(nums) - 1)
            m1 = nums[index - 1]
            m2 = nums[index]
            return (m1 + m2) / 2
        else:
            index = self.find_kth_largest_num(nums, int(len(nums) / 2) + 1, 0, len(nums) - 1)
            return nums[index]


if __name__ == '__main__':
    sol = Solution()
    nums1 = [1, 2, 3]
    nums2 = [1, 2, 2]
    print(sol.findMedianSortedArrays(nums1, nums2))
