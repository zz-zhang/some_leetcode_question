from typing import *
from pprint import pprint

class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        graph = {city: [] for city in range(n)}
        reverse_graph = {city: [] for city in range(n)}
        for s, e in edges:
            graph[s].append(e)
            reverse_graph[e].append(s)
        
        # pprint(reverse_graph)
        # pprint(graph)
        res = [[] for node in range(n)]
        visited = [False for _ in range(n)]
        for node in range(n):
            if len(graph[node]) == 0 and len(reverse_graph[node]) != 0:
                res[node] = self.dfs(reverse_graph, node, res, visited)
                print(node)
        
        for idx, sub_res in enumerate(res):
            res[idx] = sorted(sub_res)
        pprint(res)
        return res
            
    def dfs(self, graph, node, res, visited):
        visited[node] = True
        if len(graph[node]) == 0:
            return [node]
        for acient in graph[node]:
            if not visited[acient]:
                res[node] = list(set(res[node] + self.dfs(graph, acient, res, visited) + [acient]))
            else:
                res[node] = list(set(res[node] + res[acient] + [acient]))
        return res[node]

if __name__ == '__main__':
    sol = Solution()
    n = 9
    edgeList = [[7,5],[2,5],[0,7],[0,1],[6,1],[2,4],[3,5]]
    sol.getAncestors(n, edgeList)