class Solution:
    results = []

    def dfs(self, candidates, target, result):
        if target == 0:
            self.results.append(result)
            return result
        for index in range(0, len(candidates)):
            target -= candidates[index]
            if target >= 0:
                self.dfs(candidates[index:], target, result + [candidates[index]])
            target += candidates[index]

    def combinationSum(self, candidates, target):
        self.results = []
        self.dfs(candidates, target, [])
        # print(self.results)
        return self.results

if __name__ == '__main__':
    sol = Solution()
    candidates = [2,3,5]
    target = 8
    print(sol.combinationSum(candidates, target))
