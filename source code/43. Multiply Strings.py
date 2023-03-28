class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        num1 = self._str_to_list(num1)
        num2 = self._str_to_list(num2)
        
        # print(num1)
        # print(num2)
        
        res = [0 for _ in range(401)]
        for i, n1 in enumerate(num1):
            for j, n2 in enumerate(num2):
                res[i + j] += n1 * n2
        
        i = 0
        while i < len(res) - 1:
            if res[i] >= 10:
                res[i + 1] += res[i] // 10
                res[i] = res[i] % 10
            i += 1
        # print(res)
        res = self._list_to_str(res)
        return res
        
    def _str_to_list(self, num):
        res = [0 for _ in range(200)]
        i = 0
        while i < len(num):
            res[i] = ord(num[len(num) - 1 - i]) - ord('0')
            i += 1
        return res
    
    def _list_to_str(self, num):
        res = ''
        for n in num[::-1]:
            res = res + chr(n + ord('0'))
        while len(res) > 1 and res[0] == '0':
            res = res[1:]
        return res