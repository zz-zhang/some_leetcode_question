'''
There are n servers numbered from 0 to n - 1 connected by undirected server-to-server connections forming a network where connections[i] = [ai, bi] represents a connection between servers ai and bi. Any server can reach other servers directly or indirectly through the network.

A critical connection is a connection that, if removed, will make some servers unable to reach some other server.

Return all critical connections in the network in any order.

'''
# class Solution:
#     def criticalConnections(self, n, connections):
#         circles = []
#         for node in range(n):
#             q = []
#             route = []
#             used_node = []
#             for conn in connections:
#                 if node == conn[0]:
#                     q.append(conn[1])
#                     route.append([node, conn[1]])
#                 if node == conn[1]:
#                     q.append(conn[0])
#                     route.append([node, conn[0]])
            
#             while len(q) > 0:
#                 # print(q, route)
#                 tgt_node = q[0]
#                 for conn in connections:
#                     if  tgt_node == conn[0]:
#                         if conn[1] == node and len(route[0]) > 2:
#                             if not self.list_exist(circles, route[0]):
#                                 circles.append(route[0])
#                         elif conn[1] not in route[0]:
#                             q.append(conn[1])
#                             # used_node.append(used_node[0] + conn[1])
#                             route.append(route[0] + [conn[1]])
#                             # print(tgt_node, route[0])
#                             # breakpoint()
                    
#                     if tgt_node == conn[1]:
#                         if conn[0] == node and len(route[0]) > 2 :
#                             if not self.list_exist(circles, route[0]):
#                                 circles.append(route[0])
#                         elif conn[0] not in route[0]:
#                             q.append(conn[0])
#                             # used_node.append(used_node[0] + conn[0])
#                             route.append(route[0] + [conn[0]])
#                 q = q[1:]
#                 route = route[1:]
#         # circles = [sorted(c) for c in circles if len(c) > 2]
#         print(circles)

#         res = []
#         for conn in connections:
#             for c in circles:
#                 if conn[0] in c and conn[1] in c:
#                     break
#             else:
#                 res.append(conn)
#         return res

#     def list_exist(self, lst, tgt):
#         for l in lst:
#             for n1, n2 in zip(sorted(l), sorted(tgt)):
#                 if n1 != n2:
#                     break
#             else:
#                 return True
#         return False

class Solution:
    def criticalConnections(self, n, connections):
        color = [0 for _ in range(len(connections))]
        for conn in connections:
            pass


    def dfs(self, target, connections):
        



if __name__ == '__main__':
    sol = Solution()
    n = 10
    connections = [[1,0],[2,0],[3,0],[4,1],[5,3],[6,1],[7,2],[8,1],[9,6],[9,3],[3,2],[4,2],[7,4],[6,2],[8,3],[4,0],[8,6],[6,5],[6,3],[7,5],[8,0],[8,5],[5,4],[2,1],[9,5],[9,7],[9,4],[4,3]]

    n = 4
    connections = [[0,1],[1,2],[2,0],[1,3]]
    print(sol.criticalConnections(n, connections))