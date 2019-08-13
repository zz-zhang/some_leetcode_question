class Solution:
    def pow(self, x, n):
        if n == 0:
            return 1.0
        if n == 1:
            return x
        if n % 2 == 0:
            return self.pow(x, n / 2) ** 2
        else:
            return (self.pow(x, (n - 1) / 2) ** 2) * x

    def myPow(self, x: float, n: int):
        if x == 0:
            if n == 0:
                return 1
            return 0
        if n < 0:
            x = 1 / x
            n = -n
        return pow(x, n)


if __name__ == '__main__':
    sol = Solution()
    x = 34.45
    n = 0
    print(sol.myPow(x, n))
