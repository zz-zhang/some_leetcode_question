class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        p_end = 0
        # oper_counter = 0
        while p_end < int(len(s) / 2):
            if len(s) % (p_end + 1) != 0:
                p_end += 1
                continue
            p_idx = 0
            # breakpoint()
            for idx in range(p_end+1, len(s)):
                # oper_counter += 1
                if p_idx > p_end:
                    p_idx = 0
                if s[p_idx] != s[idx]:
                    break
                p_idx += 1
            else:
                # print(oper_counter)
                breakpoint()
                return True
            p_end += 1
        # print(oper_counter)
        return False

if __name__ == '__main__':
    sol = Solution()
    s = "aabaaba"
    print(sol.repeatedSubstringPattern(s))