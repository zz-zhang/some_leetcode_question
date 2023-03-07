import random

class Solution:
    def groupAnagrams(self, strs):
        if len(strs) == 0:
            return []

        keys = {chr(96+i): int(100000 ** (i - 1)) for i in range(1, 27)}
        res = {}
        # print(keys)
        for s in strs:
            _id = sum([keys[char] for char in s])
            print(s, _id)
            if _id in res:
                res[_id].append(s)
            else:
                res[_id] = [s]
        return list(res.values())

if __name__ == '__main__':
    sol = Solution()
    strs = ["a"]
    strs = [''.join([chr(random.randint(97, 97+25)) for __ in range(10000)]) for _ in range(100)]
    # print(strs[0])
    print(sol.groupAnagrams(strs))
