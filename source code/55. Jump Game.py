class Solution:
    def reachable(self, nums, target, max_length, accessable):
        # print(target)
        if target == 0:
            return True
        for i in range(max_length, 0, -1):
            if target - i >= 0 and nums[target - i] >= i and accessable[target - i] == 1:
                if self.reachable(nums, target - i, max_length, accessable):
                    return True
        accessable[target] = 0
        return False

    def canJump(self, nums) -> bool:
        max_length = max(nums)
        accessable = [1 for _ in nums]
        return self.reachable(nums, len(nums) - 1, max_length, accessable)

if __name__ == '__main__':
    sol = Solution()
    nums = [2,0,6,9,8,4,5,0,8,9,1,2,9,6,8,8,0,6,3,1,2,2,1,2,6,5,3,1,2,2,6,4,2,4,3,0,0,0,3,8,2,4,0,1,2,0,1,4,6,5,8,0,7,9,3,4,6,6,5,8,9,3,4,3,7,0,4,9,0,9,8,4,3,0,7,7,1,9,1,9,4,9,0,1,9,5,7,7,1,5,8,2,8,2,6,8,2,2,7,5,1,7,9,6]
    print(sol.canJump(nums))
