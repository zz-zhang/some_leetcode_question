from random import randint


class Solution:
    def validPalindrome(self, s: str) -> bool:
        s = list(s)
        i = 0
        j = len(s) - 1
        deleted = False
        while i < j:
            if s[i] != s[j]:
                ii = i
                jj = j

                i = i + 1
                while i < j:
                    if s[i] != s[j]:
                        break
                    i += 1
                    j -= 1
                else:
                    # print(f'del in front idx {ii}')
                    return True
                i = ii
                j = jj
                j = j - 1
                while i < j:
                    if s[i] != s[j]:
                        break
                    i += 1
                    j -= 1
                else:
                    # print(f'del in back idx: {jj}')
                    return True
                return False

            i += 1
            j -= 1
        return True

if __name__ == '__main__':
    sol = Solution()
    s = [chr(randint(97, 97+25)) for _ in range(10 ** 2)]
    s = s + ['sb'] +  s[::-1] + ['a']
    s = ''.join(s)
    s="abc"
    print(sol.validPalindrome(s))