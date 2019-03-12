class Solution:
    def mult(self, k, div):
        res = 0
        while k > 0:
            k -= 1
            res += div
        return res

    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        res = 0
        flag1 = 1
        if dividend < 0:
            flag1 = -1
            dividend = -dividend
        flag2 = 1
        if divisor < 0:
            flag2 = -1
            divisor = -divisor
        divlst = []
        scope = []
        scope.append(1)
        divlst.append(divisor)
        scope.append(10)
        divlst.append(self.mult(10, divisor))
        scope.append(100)
        divlst.append(self.mult(100, divisor))
        scope.append(1000)
        divlst.append(self.mult(1000, divisor))
        scope.append(10000)
        divlst.append(self.mult(10000, divisor))
        # scope.append(100000)
        # divlst.append(self.mult(100000, divisor))

        p = 4
        while dividend >= divisor:
            # print(ndiv)
            ndiv = divlst[p]
            if dividend >= ndiv:
                dividend -= ndiv
                res += scope[p]
            elif p > 0:
                p -= 1

        if flag1 == -1:
            res = -res
        if flag2 == -1:
            res = -res

        if res <  -2147483648:
            res = -2147483648
        if res > 2147483647:
            res = 2147483647

        return res

if __name__=='__main__':
    sol = Solution()
    print(sol.divide(-1563745632, 928683913))