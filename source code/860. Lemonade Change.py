from typing import List
from random import randint, choice

class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        self.cash = {n:0 for n in [5, 10, 20]}
        for bill in bills:
            self.cash[bill] += 1
            if bill != 5:
                if not self.change(bill-5):
                    return False
        return True

    def change(self, amount):
        if amount == 15:
            if self.cash[10] >= 1 and self.cash[5] >= 1:
                self.cash[10] -= 1
                self.cash[5] -= 1
                return True
            if self.cash[5] >= 3:
                self.cash[5] -= 3
                return True
            return False
        if amount == 5:
            if self.cash[5] >= 1:
                self.cash[5] -= 1
                return True
            return False

if __name__ == '__main__':
    sol = Solution()
    bills = [5,5,10,10,20]
    bills = [choice([5, 10, 20]) for _ in range(10000)]
    bills = sorted(bills)
    print(bills)
    print(sol.lemonadeChange(bills))