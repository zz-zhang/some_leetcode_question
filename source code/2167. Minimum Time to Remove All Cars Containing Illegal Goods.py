from random import randint


class Solution:
    def minimumTime(self, s: str):
        i = 0
        j = len(s) - 1
        while i < len(s) and s[i] == '1':
            i += 1
        while j >= 0 and s[j] == '1':
            j -= 1
        if i > j:
            return len(s)
        res = i + (len(s) - 1 - j)
        s = s[i: j + 1]
        print(i, j, s, res)

        i = 0
        zeros = []
        ones = []
        current = 0
        counter = 0
        while i < len(s):
            if int(s[i]) == current:
                counter += 1
            else:
                if current == 0:
                    zeros.append(counter)
                else:
                    ones.append(counter)
                current = 1 - current
                counter = 1
            i += 1
        else:
            zeros.append(counter)
        print(zeros, ones)

        i = 0
        j = len(zeros) - 1
        moved_i = True
        moved_j = True
        left_zeros = 0
        right_zeros = 0
        while i < j:
            remove_left = False
            remove_right = False
            
            if moved_i:
                left_zeros = left_zeros + zeros[i]
            if left_zeros > ones[i]:
                left_res = 2 * ones[i]
            else:
                left_res = left_zeros + ones[i]
                remove_left = True

            if moved_j:
                right_zeros = right_zeros + zeros[j]
            if right_zeros > ones[j-1]:
                right_res = 2 * ones[j-1]
            else:
                right_res = right_zeros + ones[j-1]
                remove_right = True
            # breakpoint()

            if left_res < right_res:
                res += left_res
                i += 1
                moved_i = True
                moved_j = False
                if remove_left:
                    left_zeros = 0
            elif left_res > right_res:
                res += right_res
                j -= 1
                moved_j = True
                moved_i = False
                if remove_right:
                    right_zeros = 0
            else:
                if remove_left:
                    res += left_res
                    i += 1
                    moved_i = True
                    moved_j = False
                    left_zeros = 0
                elif remove_right:
                    res += right_res
                    j -= 1
                    moved_j = True
                    moved_i = False
                    right_zeros = 0
                else:
                    res += left_res
                    i += 1
                    moved_i = True
                    moved_j = False
        return res

if __name__ == '__main__':
    sol = Solution()
    s = "1101110100001010010111111110110000100010111010000001001001110101010011111011101111000101111111001000"
    # s = ''.join([str(randint(0,1)) for _ in range(100)])
    print(s)
    print(sol.minimumTime(s))