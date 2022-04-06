from typing import List
from random import randint
class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        n = len(rooms)
        graph = {idx: nodes for idx, nodes in enumerate(rooms)}
        visited = [0 for _ in range(n)]
        visited[0] = 1
        self.dfs(graph, 0, visited)
        # print(visited)
        return all(visited)

    def dfs(self, graph, node, visited):
        # print(node, graph[node])
        for next_node in graph[node]:
            if visited[next_node] == 0:
                visited[next_node] = 1
                self.dfs(graph, next_node, visited)


if __name__ == '__main__':
    sol = Solution()
    rooms = [[1], []]
    n = 5
    rooms = [[randint(0, n) for _ in range(randint(0, n) + 1)] for __ in range(n + 1)]
    print(rooms)
    print(sol.canVisitAllRooms(rooms))