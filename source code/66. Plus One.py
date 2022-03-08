class Solution:
    def plusOne(self, digits):
        digits[-1] = digits[-1] + 1
        idx = len(digits) - 1
        while idx >= 0:
            if digits[idx] >= 10:
                digits[idx] -= 10
                if idx > 0:
                    digits[idx - 1] += 1
                else:
                    digits = [1] + digits
            else:
                break
            idx -= 1
        return digits


if __name__ == '__main__':
    import random
    sol = Solution()
    digits = [random.randint(1, 9)] + [random.randint(0, 9) for _ in range(99)]
    print(digits)
    print(sol.plusOne(digits))
        