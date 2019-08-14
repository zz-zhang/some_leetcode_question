class Solution:
    def canJump(self, nums) -> bool:
        if len(nums) == 0:
            return True
        reachable = [0 for _ in nums]
        reachable[0] = 1
        for i in range(0, len(nums) - 1):
            if reachable[i] == 1:
                for j in range(1, nums[i] + 1):
                    if i + j < len(nums):
                        reachable[i + j] = 1
        # print(reachable)
        if reachable[len(nums) - 1] == 1:
            return True
        else:
            return False

if __name__ == '__main__':
    sol = Solution()
    nums = [2, 0]
    print(sol.canJump(nums))
