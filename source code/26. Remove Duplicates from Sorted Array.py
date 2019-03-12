
class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) > 0:
            buff = nums[0]
        i = 1
        while i < len(nums):
            if i >= len(nums):
                break
            if buff == nums[i]:
                nums.remove(nums[i])
                i -= 1
            else:
                buff = nums[i]
            i += 1
        return len(nums)

if __name__ == '__main__':
    num = []
    sol = Solution()
    print(sol.removeDuplicates(num))