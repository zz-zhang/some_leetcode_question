from random import randint

class Solution:
    def partitionString(self, s: str) -> int:
        res = 0
        start = 0
        # cache = []
        while start < len(s):
            end = start
            saved = set()
            while end < len(s):
                if s[end] not in saved:
                    saved.add(s[end])
                    end += 1
                else:
                    break
            # cache.append(s[start:end])
            res += 1
            start = end
        # print(cache)
        return res

if __name__ == '__main__':
    sol = Solution()
    s = "abacaba"
    s = ''.join([chr(randint(97, 97+25)) for _ in range(100000)])
    print(s)
    print(sol.partitionString(s))