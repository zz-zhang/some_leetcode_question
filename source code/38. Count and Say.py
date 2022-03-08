class Solution:
    def countAndSay(self, n):
        if n == 1:
            return '1'
        else:
            pre_res = self.countAndSay(n - 1)
            # print(pre_res)
            return self.say(pre_res)
    
    def say(self, s):
        counter = 0
        currect_num = ''
        res = ''
        # print(s)
        # breakpoint()
        for idx, num in enumerate(s):
            if currect_num == '' or currect_num == num:
                currect_num = num
                counter += 1
            else:
                res = res + str(counter) + currect_num
                currect_num = num
                counter = 1
        res = res + str(counter) + num
        return res


if __name__ == '__main__':
    sol = Solution()
    n = 30
    print(sol.countAndSay(n))
        