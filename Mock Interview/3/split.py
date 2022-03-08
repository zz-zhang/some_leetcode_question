'''
You are given a string s. We want to partition the string into as many parts as possible so that each letter appears in at most one part.

Note that the partition is done so that after concatenating all the parts in order, the resultant string should be s.

Return a list of integers representing the size of these parts.
'''
class Solution:
    def partitionLabels(self, s: str):

        chars = []
        start_idx = []
        end_idx = []
        for idx, char in enumerate(s):
            if char not in chars:
                chars.append(char)
                start_idx.append(idx)
                end_idx.append(idx)
            else:
                end_idx[chars.index(char)] = idx

        # for char, s, e in zip(chars, start_idx, end_idx):
        #     print(char, s, e)
        res = self.merge_parts(start_idx, end_idx)
        return res

    def merge_parts(self, s_idx, e_idx):
        merged = [False for _ in range(len(s_idx))]
        res = []
        for i in range(len(s_idx)):
            sub_res = 0
            s = s_idx[i]
            e = e_idx[i]
            # breakpoint()
            if not merged[i]:
                for j in range(i+1, len(s_idx)):
                    if not merged[j]:
                        sub_s, sub_e = self.merge(s, e, s_idx[j], e_idx[j])
                        # breakpoint()
                        if sub_s is not None:
                            s = sub_s
                            e = sub_e
                            merged[i] = True
                            merged[j] = True
                sub_res = e - s + 1
                if sub_res != 0:
                    merged[i] = True
                    res.append(sub_res)
        return res
        
    def merge(self, s1, e1, s2, e2):
        if s2 > e1 or e2 < s1:
            return None, None
        else:
            return min(s1, s2), max(e1, e2)
            


if __name__ == '__main__':
    sol = Solution()
    s = "caedbdedda"
    s2= 'eccbbbbdec'
    print(sol.partitionLabels(s2))        