class Solution:
    def maxLength(self, arr):
        total = ''.join(arr)
        total_len = len(total)
        all_repeated = ''
        seen = ''
        for s in total:
            if s not in seen:
                seen = seen + s
            else:
                all_repeated = all_repeated + s
        all_repeated = set(all_repeated)

        while len(all_repeated) > 0:
            num_repeated = [len(list(all_repeated.intersection(set(s)))) for s in arr]
            arr = [x for _, x in sorted(zip(num_repeated, arr), reverse=True)]
            total_len -= len(arr[0])
            all_repeated = all_repeated - set(arr[0])
            arr = arr[1:]
            # print(all_repeated)
        return total_len


if __name__ == '__main__':
    sol = Solution()
    arr =  ["un","iq","ue"]
    print(sol.maxLength(arr))