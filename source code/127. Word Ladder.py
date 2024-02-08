from typing import List

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        visited = set([beginWord])
        q = [(beginWord, 1)]

        while q:
            cur_word, num_step = q.pop(0)
            # print(cur_word, num_step)

            if cur_word == endWord:
                return num_step

            for word in wordList:
                if word not in visited:
                    if self.distance(cur_word, word) == 1:
                        q.append((word, num_step + 1))
                        visited.add(word)
        return 0

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
    beginWord = "hit"
    endWord = "cog"
    wordList = ["hot","dot","dog","lot","log","cog"]

    print(sol.ladderLength(beginWord, endWord, wordList))