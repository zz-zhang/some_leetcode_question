from random import randint


class Solution:
    def sortEvenOdd(self, nums):
        even = [n for idx, n in enumerate(nums) if idx % 2 == 0]
        odd = [n for idx, n in enumerate(nums) if idx % 2 == 1]
        even = sorted(even)
        odd = sorted(odd, reverse=True)

        res = []
        i = 0
        j = 0
        while i < len(even) or j < len(odd):
            if i < len(even):
                res.append(even[i])
                i += 1
            if j < len(odd):
                res.append(odd[j])
                j += 1
        return res

if __name__ == '__main__':
    sol = Solution()
    nums = [randint(1, 100) for _ in range(99)]
    print(nums)
    print(sol.sortEvenOdd(nums))
        