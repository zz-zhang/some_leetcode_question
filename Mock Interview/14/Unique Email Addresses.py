from random import randint
from typing import *

class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        recoder = {}
        for email in emails:
            local, host = email.split('@')
            local = local.replace('.', '')
            if '+' in local:
                local = local[:local.index('+')]
            
            # print(local)

            if local not in recoder.keys():
                recoder[local] = [host]
            elif host not in recoder[local]:
                recoder[local].append(host)

        counter = 0
        for local in recoder.keys():
            counter += len(recoder[local])

        return counter


if __name__ == '__main__':
    sol = Solution()
    emails = ["test.email+a+lex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]
    print(sol.numUniqueEmails(emails))