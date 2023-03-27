class Solution:
    def isHappy(self, n: int) -> bool:
        visited = set()
        num = n
        while num not in visited:
            # print(num, end=' ')
            visited.add(num)
            num = self.split(num)
            # print(num)
            if num == 1:
                return True
        return False

    def split(self, n):
        res = 0
        while n > 0:
            # print(res)
            # breakpoint()
            res = res + (n % 10) ** 2
            n = n // 10
        return res


if __name__ == '__main__':
    sol = Solution()
    n = 2
    print(sol.isHappy(n))