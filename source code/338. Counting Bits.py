'''
in O(n)
'''

class Solution:
    def countBits(self, n: int):
        if n == 0:
            return [0]
        res = [0, 1]
        index = 1
        for num in range(2, n + 1):
            if num == 2 ** index:
                res.append(1)
            else:
                res.append(res[2 ** index] + res[num - 2 ** index])
            
            if num == 2 ** (index + 1) - 1:
                index += 1

        # print(self.brute(n) == res)
        return res
    
    def brute(self, n):
        binary = [0]
        res = [0]
        while n > 0:
            binary[-1] += 1
            index = -1
            while binary[index] == 2:
                binary[index] = 0
                if index == -len(binary):
                    binary = [1] + binary
                else:
                    binary[index - 1] += 1
                index -= 1
            # print(binary, sum(binary))
            res.append(sum(binary))
            n -= 1
        return res


if __name__ == '__main__':
    sol = Solution()
    n = 100000 # [0, 100000 (< 2 ** 17)]
    print(sol.countBits(n))