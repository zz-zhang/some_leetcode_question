class Solution:
    def makesquare(self, matchsticks):
        if sum(matchsticks) % 4 != 0:
            return False
        edge_len = int(sum(matchsticks) / 4)
        edge = [[0]]
        for idx, match in enumerate(matchsticks):
            idx = idx + 1
            poss = []
            for prev_idx in range(idx):
                new_edge_lens = [match + match2 for match2 in edge[prev_idx] if match+match2 <= edge_len]
                poss = poss + new_edge_lens
            edge.append(poss)
        print(edge)
        good_edges = [length for possible_length in edge for length in possible_length if length == edge_len]
        print(good_edges)
        if len(good_edges) == 4:
            return True
        return False

if __name__ == '__main__':
    sol = Solution()
    matchsticks = [1,1,2,2,3,3,4]
    print(sol.makesquare(matchsticks))
        