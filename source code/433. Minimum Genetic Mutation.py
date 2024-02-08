from typing import List

class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        q = [(startGene, 0)]
        visited = set([startGene])
        while q:
            current_gene, num_step = q.pop(0)
            if current_gene == endGene:
                return num_step
            for saved_gene in bank:
                if self.distance(current_gene, saved_gene) == 1 and saved_gene not in visited:
                    q.append((saved_gene, num_step + 1))
                    visited.add(saved_gene)
        return -1

    def distance(self, s1, s2):
        count = 0
        for c1, c2 in zip(s1, s2):
            if c1 != c2:
                count += 1
            if count >= 2:
                return count
        return count

if __name__ == '__main__':
    sol = Solution()
    startGene = "AACCGGTT"
    endGene = "AAACGGTA"
    bank = ["AACCGGTA","AACCGCTA","AAACGGTA"]
    print(sol.minMutation(startGene, endGene, bank))