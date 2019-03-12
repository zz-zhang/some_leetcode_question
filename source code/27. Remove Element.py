class Solution:
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        i = 0
        while val in nums:
            nums.remove(val)
        return len(nums)

if __name__ == '__main__':
    sol = Solution()
    nums = [3,2,2,3]
    val = 3
    print(sol.removeElement(nums, val))