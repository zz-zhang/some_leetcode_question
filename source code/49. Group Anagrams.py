class Solution:
    def groupAnagrams(self, strs):
        if len(strs) == 0:
            return []
        # hash crash exists
        # ----------
        # result = []
        # sub_res = []
        # while '' in strs:
        #     strs.remove('')
        #     sub_res.append('')
        # if len(sub_res) != 0:
        #     result.append(sub_res)
        # hash_xor = []
        #
        # for s in strs:
        #     h = ord(s[0])
        #     for c in s[1:]:
        #         h = h ^ ord(c)
        #     hash_xor.append(h)
        # used = []
        # for i in range(0, len(hash_xor)):
        #     if hash_xor[i] not in used:
        #         sub_res = []
        #         used.append(hash_xor[i])
        #         sub_res.append(strs[i])
        #         for j in range(i + 1, len(hash_xor)):
        #             if hash_xor[i] == hash_xor[j]:
        #                 sub_res.append(strs[j])
        #         result.append(sub_res)
        # return result
        # ----------
        sorted_strs = [s for s in strs]
        strs_pair = []
        for index in range(0, len(strs)):
            sorted_strs[index] = ''.join(sorted(strs[index]))
            strs_pair.append((strs[index], sorted_strs[index]))

        strs_pair = sorted(strs_pair, key=lambda x:(x[1], x[0]))
        # print(strs_pair)

        result = []
        sub_res = [strs_pair[0][0]]
        index = 1
        while index < len(strs_pair):
            if strs_pair[index][1] == strs_pair[index - 1][1]:
                sub_res.append(strs_pair[index][0])
            else:
                result.append(sub_res)
                sub_res = [strs_pair[index][0]]
            index += 1
        result.append(sub_res)
        return result

if __name__ == '__main__':
    sol = Solution()
    strs =  ["eat", "tea", "tan", "ate", "nat", "bat"]
    print(sol.groupAnagrams(strs))
