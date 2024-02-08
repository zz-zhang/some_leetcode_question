from typing import List

class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        flatten = [row if not idx % 2 else row[::-1] for idx, row in enumerate(board[::-1])]
        flatten = [item - 1 if item != -1 else item for row in flatten for item in row]
        # print(len(flatten))
        # print(flatten)
        q = [(0, 0)]
        visited = set([0])
        while q:
            curr_idx, num_step = q.pop(0)
            # print(curr_idx, num_step)
            if curr_idx == len(flatten) - 1:
                return num_step

            for step in range(1, 7):
                if curr_idx + step < len(flatten):
                    if flatten[curr_idx + step] == -1:
                        if curr_idx + step not in visited:
                            q.append((curr_idx + step, num_step + 1))
                            visited.add(curr_idx + step)
                    else:
                        if flatten[curr_idx + step] not in visited:
                            q.append((flatten[curr_idx + step], num_step + 1))
                            visited.add(flatten[curr_idx + step])
        return -1


if __name__ == '__main__':
    sol = Solution()
    board = [
        [1,1,-1],
        [1,1,1],
        [-1,1,1]]
    print(sol.snakesAndLadders(board))