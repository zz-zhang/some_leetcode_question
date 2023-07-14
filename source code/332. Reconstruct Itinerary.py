from typing import List
from random import randint

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        self.routes = {}
        for src, tgt in tickets:
            if src not in self.routes:
                self.routes[src] = [tgt]
            else:
                self.routes[src].append(tgt)
        self.routes = {src: sorted(tgt) for src, tgt in self.routes.items()}
        # print(self.routes)
        res = self.search('JFK', len(tickets), ['JFK'])
        return res

    def search(self, src, remaining_steps, res=[]):
        if remaining_steps == 0:
            return res
        if src not in self.routes or not self.routes[src]:
            return None

        for idx, tgt in enumerate(self.routes[src]):
            self.routes[src].pop(idx)
            sub_res = self.search(tgt, remaining_steps-1, res+[tgt])
            self.routes[src].insert(idx, tgt)
            if sub_res:
                return sub_res
        return None
        

if __name__ == '__main__':
    sol = Solution()
    tickets = [["JFK","KUL"],["JFK","NRT"],["NRT","JFK"]]
    print(tickets)
    print(sol.findItinerary(tickets))
