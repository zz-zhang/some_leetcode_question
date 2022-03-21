from typing import *
class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        tuples = []
        for char, idx in zip(s, indices):   
            tuples.append((char, idx))
        tuples = sorted(tuples, key=lambda x:x[1])
        # print(tuples)
        tuples = [t[0] for t in tuples]
        return ''.join(tuples)

if __name__ == '__main__':
    sol = Solution()
    s = "c"
    indices = [0]
    print(sol.restoreString(s, indices))