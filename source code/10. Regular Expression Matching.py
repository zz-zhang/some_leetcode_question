class Solution:


    def match_fragment(self, s, fragment, start_flag):
        if start_flag + len(fragment) > len(s):
            return False
        for i in range(start_flag, start_flag + len(fragment)):
            if fragment[i - start_flag] != '.' and\
                    s[i] != fragment[i - start_flag]:
                return False
        return True


    def find_location(self, s, fragment, start_flag, allow_ignore):
        s = str(s)
        for i in range(start_flag, len(s)):
            if self.match_fragment(s, fragment, i):
                return i, i + len(fragment)
            if allow_ignore and self.match_fragment(s, fragment[:len(fragment) - 1], i):
                return i, i + len(fragment) - 1
        return -1, -1


    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        alphabet = [chr(a) for a in range(97, 97 + 26)]
        alphabet.append(',')
        s = s + ','
        p = p + ','
        matched_s = [False for i in range(0, len(s))]

        shortest_p = str(p)
        for alpha in alphabet:
            shortest_p = shortest_p.replace(alpha + '*', '')
        if len(shortest_p) > len(s):
            return False

        last_is_star = False
        splited_p = p.split('*')
        if p[-1] == '*':
            last_is_star = True
            splited_p = splited_p[:len(splited_p) - 1]
        # print(splited_p)
        start_flag = []
        end_flag = []
        for fragment in splited_p:
            if len(end_flag) == 0:
                start = 0
            else:
                start = end_flag[-1]
            allow_ignore = True
            if fragment == splited_p[-1] and not last_is_star:
                allow_ignore = False

            start_flag_temp, end_flag_temp = self.find_location(s, fragment, start, allow_ignore)
            if start_flag_temp != -1:
                start_flag.append(start_flag_temp)
                end_flag.append(end_flag_temp)
                # print(start_flag)
                # print(end_flag)
                # return False

        for iter_flag in range(0, len(start_flag)):
            for iter_matched in range(start_flag[iter_flag], end_flag[iter_flag]):
                matched_s[iter_matched] = True

        start_flag.append(len(s))
        for iter_flag in range(0, len(start_flag) - 1):
            start = end_flag[iter_flag]
            end = start_flag[iter_flag + 1]
            for finder in range(start, end):
                if s[finder] != s[start]:
                    # return False
                    break
                else:
                    matched_s[finder] = True


        # print(start_flag)
        # print(end_flag)
        print(matched_s)
        for iter_matched in matched_s:
            if not iter_matched:
                return False

        return True




if __name__ == '__main__':
    s = 'aaa'
    p = 'ab*a'
    sol = Solution()
    print(sol.isMatch(s, p))