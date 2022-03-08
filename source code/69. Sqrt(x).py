class Solution:
    def mySqrt(self, x):
        res = 0
        while res <= x:
            if res ** 2 >= x:
                if res ** 2 == x:
                    return res
                else:
                    return res - 1
            res += 1
        return res

if __name__ == '__main__':
    sol = Solution()
    x = 2
    print(sol.mySqrt(x))