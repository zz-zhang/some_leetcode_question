'''You are given an array representing a row of seats where seats[i] = 1 represents a person sitting in the ith seat, and seats[i] = 0 represents that the ith seat is empty (0-indexed).

There is at least one empty seat, and at least one person sitting.

Alex wants to sit in the seat such that the distance between him and the closest person to him is maximized. 

Return that maximum distance to the closest person.'''

class Solution:
    def maxDistToClosest(self, seats):
        occupied = [idx for idx, state in enumerate(seats) if state == 1]
        # print(occupied)
        res = -1
        res = max(occupied[0] - 0, len(seats) - 1 - occupied[-1])
        # print(res)
        for loc1, loc2 in zip(occupied[:-1], occupied[1:]):
            res = max(res, int((loc2 - loc1)/2))
            # print(res)

        return res


if __name__ == '__main__':
    sol = Solution()
    seats = [1,0,0,1,0,0,0,1,0,0,0]
    print(sol.maxDistToClosest(seats))
        