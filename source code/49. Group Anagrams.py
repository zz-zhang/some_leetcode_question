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
        for index in range(0, len(strs)):
            sorted_strs[index] = ''.join(sorted(strs[index]))
        # print(sorted_strs)

        result = []
        used = []
        for i in range(0,len(strs)):
            if sorted_strs[i] not in used:
                used.append(sorted_strs[i])
                sub_res = [strs[i]]
                for j in range(i + 1, len(strs)):
                    if sorted_strs[i] == sorted_strs[j]:
                        sub_res.append(strs[j])
                result.append(sub_res)
        return result

if __name__ == '__main__':
    sol = Solution()
    strs = ["","", "abc", "cba", "abd"]
    print(sol.groupAnagrams(strs))
