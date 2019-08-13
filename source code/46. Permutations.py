class Solution:
    results = []
    def dfs(self, candidates, result):
        if len(candidates) == 1:
            self.results.append(result + [candidates[0]])
            return result
        for index in range(0, len(candidates)):
            # result.append(candidates[index])
            self.dfs(candidates[:index] + candidates[index+1:], result + [candidates[index]])
    def permute(self, nums):
        self.results = []
        if len(nums) == 0:
            return [[]]
        self.dfs(nums, [])
        return self.results

if __name__ == '__main__':
    sol = Solution()
    a = [1,2,3]
    # print(a[:2] + a[3:])
    nums = [1,2,3]
    print(sol.permute(nums))
