class Solution:
    def climbStairs(self, n):
        fe = [1, 2]
        for idx in range(2, n):
            fe.append(fe[idx-1] + fe[idx-2])
        return fe[n-1]

if __name__ == '__main__':
    sol = Solution()
    n = 4
    print(sol.climbStairs(n))