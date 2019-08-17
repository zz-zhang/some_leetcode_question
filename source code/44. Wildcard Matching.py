class Solution:
    alphabet = [chr(i) for i in range(97, 97 + 26)]
    def only_star(self, s):
        if '?' in s:
            return False
        for alpha in self.alphabet:
            if alpha in s:
                return False
        return True

    def match(self, sub_s, sub_p):
        if len(sub_p) == 0:
            if len(sub_s) == 0:
                return True
            else:
                return False
        if len(sub_s) == 0:
            if self.only_star(sub_p):
                return True
            else:
                return False

        if sub_p[0] == '?':
            return self.match(sub_s[1:], sub_p[1:])
        elif sub_p[0] == '*':
            if len(sub_p) == 1:
                return True
            else:
                # start_index = 0
                # next_alpha = -1
                # for a in sub_p:
                #     if a in self.alphabet:
                #         next_alpha = a
                #         break
                # else:
                #     q_mark_len = 0
                #     for a in sub_p:
                #         if a == '?':
                #             q_mark_len += 1
                #     if q_mark_len <= len(sub_s):
                #         return True
                #     else:
                #         return False
                # index = sub_s.find(next_alpha, start_index)
                # while index != -1:
                #     if self.match(sub_s[index:], sub_p[1:]):
                #         return True
                #     start_index = index + 1
                #     index = sub_s.find(next_alpha, start_index)
                for index in range(0, len(sub_s)):
                    if self.match(sub_s[index:], sub_p[1:]):
                        return True
                return False

        elif sub_p[0] == sub_s[0]:
            return self.match(sub_s[1:], sub_p[1:])
        return False

    def isMatch(self, s: str, p: str) -> bool:
        self.alphabet = [chr(i) for i in range(97, 97 + 26)]
        return self.match(s, p)

if __name__ == '__main__':
    sol = Solution()
    s = 'aa'
    p = 'a'
    print(sol.isMatch(s, p))
