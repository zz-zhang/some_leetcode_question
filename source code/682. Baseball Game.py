from typing import List


class Solution:

    def calPoints(self, ops: List[str]) -> int:
        record = []
        for o in ops:
            if o not in 'CD+':
                record.append(int(o))
            elif o == 'C':
                record.pop()
            elif o == 'D':
                record.append(2 * record[-1])
            else:
                record.append(record[-1] + record[-2])
        return sum(record)


if __name__ == '__main__':
    sol = Solution()
    ops = ['1']
    print(sol.calPoints(ops))
