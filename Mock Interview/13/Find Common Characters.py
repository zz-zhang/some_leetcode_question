class Solution:
    def commonChars(self, words: list[str]) -> list[str]:
        res = sorted(list(words[0]))
        for word in words[1:]:
            word = sorted(list(word))
            res = self.common_elements(res, word)
        # print(res)
        return res

    def common_elements(self, l1, l2):
        visited = [False for _ in range(len(l2))]
        res = []
        i = 0
        # print(l1, l2)
        while i < len(l1):
            j = 0
            while j < len(l2):
                if l1[i] == l2[j] and not visited[j]:
                    res.append(l1[i])
                    visited[j] = True
                    break
                j += 1
            i += 1
        return res


if __name__ == '__main__':
    sol = Solution()
    words = ["cool","apik","cook"]
    print(sol.commonChars(words))