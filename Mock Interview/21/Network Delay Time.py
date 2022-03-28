from typing import *
from pprint import pprint
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        k -= 1
        dis = [10 ** 9 for _ in range(n)]
        dis[k] = 0
        s = [k]
        u = [node for node in range(n) if node != k]
        graph = {node: {node2: 10 ** 9 for node2 in range(n)} for node in range(n)}

        for start, end, weight in times:
            graph[start - 1][end - 1] = min(weight, graph[start - 1][end - 1])

        # pprint(graph)
        while len(u) > 0:
            min_dis = 10 ** 9
            next_node = -1
            for s_node in s:
                for u_node in u:
                    if min_dis > dis[s_node] + graph[s_node][u_node]:
                        min_dis = dis[s_node] + graph[s_node][u_node]
                        next_node = u_node
            # print(next_node, mid_node, min_dis, dis[mid_node])
            if next_node == -1:
                break
            dis[next_node] = min_dis
            s.append(next_node)
            u.remove(next_node)
        res = max(dis)
        if res >= 10 ** 9:
            return -1
        return res

if __name__ == '__main__':
    sol = Solution()
    times = [[3,5,78],[2,1,1],[1,3,0],[4,3,59],[5,3,85],[5,2,22],[2,4,23],[1,4,43],[4,5,75],[5,1,15],[1,5,91],[4,1,16],[3,2,98],[3,4,22],[5,4,31],[1,2,0],[2,5,4],[4,2,51],[3,1,36],[2,3,59]]
    n = 5
    k = 5
    print(sol.networkDelayTime(times, n, k))
