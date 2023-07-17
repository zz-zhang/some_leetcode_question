from typing import List
from random import randint, choice

class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        people = sorted(people, key=lambda x:(x[0], x[1]))
        # print(people)
        for idx in range(len(people)-1, -1, -1):
            h, k = people[idx]
            if  (idx - k >= 0 and people[idx - k][0] >= h) and (idx - k - 1 < 0 or people[idx - k - 1][0] < h):
                # print('skip', people[idx])
                continue
            
            # print('exchange', people[idx])
            num_swap = k
            satified_idx = idx - 1
            while satified_idx >= 0 and people[satified_idx][0] >= h:
                satified_idx -= 1
                num_swap -= 1

            current_idx = idx
            while num_swap > 0:
                people[current_idx], people[current_idx+1] = people[current_idx+1], people[current_idx]
                num_swap -= 1
                current_idx += 1
            # print(people)
        return people
            


if __name__ == '__main__':
    sol = Solution()
    people = [[6,0],[5,0],[4,0],[3,2],[2,2],[1,4]]
    print(people)
    print(sol.reconstructQueue(people))