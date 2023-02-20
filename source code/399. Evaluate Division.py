from typing import List

from numpy import append

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float],
                    queries: List[List[str]]) -> List[float]:
        """
        from https://leetcode.com/problems/evaluate-division/discuss/1992951/Python-oror-DFS-Solution
        """
        graph = defaultdict(dict)

        for (x, y), value in zip(equations, values):
            graph[x][y] = value
            graph[y][x] = 1 / value  # x / y = value => y / x = 1 / value

        def query(u: str, end: str, val: float, visited: set) -> float:
            """
            :param u: current node in the DFS traversal
            :param end: destination node in DFS traversal
            :param val: value obtained for reaching to u
            :param visited: set of all the visited node in DFS traversal
            :return: val * (value obtained for reaching from "u" to "end")
            """
            if u == end:
                return val

            visited.add(u)

            for v, w_uv in graph[u].items():
                if v not in visited:
                    # start_node / u = val and u / v = w_uv so
                    # start_node / v = val * w_uv
                    out = query(v, end, val * w_uv, visited)

                    if out > 0:  # out != -1
                        return out

            return -1

        output = []

        for a, b in queries:
            if a not in graph or b not in graph:
                # one of the variables is not in the graph
                output.append(-1)
            else:
                output.append(query(a, b, 1, set()))

        return output


# class TreeNode:

#     def __init__(self, val, sons=[]) -> None:
#         self.val = val
#         self.sons = set(sons)

#     def add_son(self, son):
#         self.sons.add(son)

# class Solution:

#     def calcEquation(self, equations: List[List[str]], values: List[float],
#                      queries: List[List[str]]) -> List[float]:
#         values = {
#             **{(n1, n2): val
#                for (n1, n2), val in zip(equations, values)},
#             **{(n1, n2): 1 / val
#                for (n2, n1), val in zip(equations, values)}
#         }
#         nodes = {}
#         for n1, n2 in equations:
#             if n1 not in nodes:
#                 node1 = TreeNode(n1)
#                 nodes[n1] = node1
#             if n2 not in nodes:
#                 node2 = TreeNode(n2)
#                 nodes[n2] = node2

#             nodes[n1].add_son(nodes[n2])
#             nodes[n2].add_son(nodes[n1])
#             # breakpoint()
#         assume = {node: None for node in nodes.keys()}
#         for node in nodes.values():
#             if assume[node.val] is None:
#                 assume[node.val] = 1.0
#                 self.dfs_assume(nodes, node, values, assume)

#         union = {node: node for node in nodes.keys()}
#         q = list(union.keys())
#         visited = set([list(union.keys())[0]])

#         while len(q) > 0:
#             n = q[0]
#             for son_node in nodes[n].sons:
#                 if son_node.val not in visited:
#                     visited.add(son_node.val)
#                     if union[son_node.val] == son_node.val:
#                         union[son_node.val] = union[n]
#                         q.append(son_node.val)
#             q = q[1:]
#         print(union)

#         result = []
#         for n1, n2 in queries:
#             if n1 not in assume or n2 not in assume or assume[
#                     n1] is None or assume[n2] is None:
#                 result.append(-1.0)
#             else:
#                 if union[n1] != union[n2]:
#                     result.append(-1.0)
#                 else:
#                     result.append(assume[n1] / assume[n2])
#         # print(assume)
#         return result

#     def dfs_assume(self, nodes, node, values, assume):
#         for son_node in nodes[node.val].sons:
#             if assume[son_node.val] is None and (son_node.val,
#                                                  node.val) in values:
#                 assume[son_node.val] = values[(son_node.val,
#                                                node.val)] * assume[node.val]
#                 self.dfs_assume(nodes, son_node, values, assume)

if __name__ == '__main__':
    sol = Solution()
    equations = [["a", "c"], ["b", "e"], ["c", "d"], ["e", "d"]]

    values = [2.0, 3.0, 0.5, 5.0]

    queries = [["a", "b"]]
    print(sol.calcEquation(equations, values, queries))
