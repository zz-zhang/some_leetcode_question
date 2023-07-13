from typing import List
from random import randint

class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        self.res = []
        self.search(s)
        return self.res

    def search(self, s, sub_res=[]):
        # print(s)
        if len(s) == 0 and len(sub_res) == 4:
            self.res.append('.'.join(sub_res))
            return True
        elif len(sub_res) == 4:
            return False

        for end in range(1, len(s) + 1):                
            temp = s[:end]
            # breakpoint()
            if temp and ((int(temp) == 0 and len(temp) == 1) or (int(temp) > 0 and temp[0] != '0')) and 0 <= int(temp) <= 255:
                self.search(s[end:], sub_res + [temp])

if __name__ == '__main__':
    sol = Solution()
    s = "010010"
    # s = ''.join([str(randint(0, 255)) for _ in range(4)])
    print(s)
    print(sol.restoreIpAddresses(s))
