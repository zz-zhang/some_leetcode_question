from typing import List

class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        res = []
        target = len(graph) - 1
        graph = {idx: nodes for idx, nodes in enumerate(graph)}
        q = [(0, [0])]
        while len(q) > 0:
            node, path = q[0]
            for next_node in graph[node]:
                if next_node not in path:
                    if next_node == target:
                        res.append(path + [next_node])
                    else:
                        q.append((next_node, path + [next_node]))
            q = q[1:]
        return res

if __name__ == '__main__':
    sol = Solution()
    graph = [[j for j in range(15) if j != i] for i in range(15)]
    # graph = [[4,3,1],[3,2,4],[3],[4],[]]
    print(graph)
    print(sol.allPathsSourceTarget(graph))
