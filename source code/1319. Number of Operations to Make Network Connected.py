from typing import List


class Solution:

    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        graph = {i: [] for i in range(n)}
        for a, b in connections:
            graph[a].append(b)
            graph[b].append(a)

        num_groups = 0
        num_edges = 0
        visited = set()
        for start in graph.keys():
            if start not in visited:
                num_groups += 1

                group = set()
                group.add(start)
                self.count_group(graph, start, visited, group)
                temp_edge = 0
                for node in group:
                    temp_edge += len(graph[node])
                num_edges += temp_edge // 2
                # print(group)

        # print(num_groups, num_edges)

        if num_edges >= n - 1:
            return num_groups - 1
        else:
            return -1

    def count_group(self, graph, node, visited, group):
        for next_node in graph[node]:
            if next_node not in visited:
                visited.add(next_node)
                group.add(next_node)
                self.count_group(graph, next_node, visited, group)
        # return edge

if __name__ == '__main__':
    sol = Solution()
    n = 4
    connections = [[0,1],[0,2],[1,2]]
    print(sol.makeConnected(n, connections))