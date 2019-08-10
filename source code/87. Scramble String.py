class Solution:

    def is_continue(self, sub_num):
        sort_num = sorted(sub_num)
        for index in range(1, len(sort_num)):
            if sort_num[index] - sort_num[index - 1] != 1:
                return False
        return True

    def is_legal(self, sub_num):
        if len(sub_num) == 1:
            return True
        if len(sub_num) == 2:
            if abs(sub_num[0] - sub_num[1]) == 1:
                return True
            else:
                return False
        else:
            flag = False
            for index in range(1, len(sub_num) - 1):
                if self.is_legal(sub_num[:index]) and self.is_legal(sub_num[index:]):
                    flag = True
                    break
            if flag and self.is_continue(sub_num):
                return True
            else:
                return False


    def isScramble(self, s1: str, s2: str) -> bool:
        num_dict = {}
        for i, c in enumerate(s1):
            num_dict[c] = i
        # print(num_dict)
        s2_num = []
        for c in s2:
            if c in num_dict:
                s2_num.append(num_dict[c])
            else:
                return False
        # print(s2_num)
        return self.is_legal(s2_num)



if __name__ == '__main__':
    sol = Solution()
    str1 = 'great'
    str2 = 'rgeat'
    print(sol.isScramble(str1, str2))
