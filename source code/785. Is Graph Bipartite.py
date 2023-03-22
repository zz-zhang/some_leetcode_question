from typing import List


class Solution:

    def isBipartite(self, graph: List[List[int]]) -> bool:
        self.graph = graph
        self.sets = {0: set(), 1: set()}

        res = True
        for node in range(len(graph)):
            if node not in self.sets[0] and node not in self.sets[1]:
                self.sets[0].add(node)
                res = res and self.dfs(node)
            if not res:
                return False

        # print(len(self.sets[0]) + len(self.sets[1]))
        # print(self.sets)
        return res and len(self.sets[0]) + len(self.sets[1]) == len(graph)

    def dfs(self, node):
        node_set = 0 if node in self.sets[0] else 1
        for next_node in self.graph[node]:
            if next_node in self.sets[0] or next_node in self.sets[0]:
                next_node_set = 0 if next_node in self.sets[0] else 1
                if node_set == next_node_set:
                    return False
                else:
                    continue
            else:
                self.sets[1 - node_set].add(next_node)

            if not self.dfs(next_node):
                return False
        return True


if __name__ == '__main__':
    sol = Solution()
    graph = [[1],[0],[4],[4],[2,3]]
    print(sol.isBipartite(graph))