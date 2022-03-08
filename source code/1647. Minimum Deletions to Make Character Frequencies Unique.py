class Solution:
    def minDeletions(self, s: str):
        counter = {}
        for char in s:
            if char in counter.keys():
                counter[char] += 1
            else:
                counter[char] = 1
        
        values = sorted(list(counter.values()))
        # print(values)
        repeated_idx = self.repeated_idx(values)
        if len(repeated_idx) == 0:
            return 0
        return self.delete(values, repeated_idx)
        

    def repeated_idx(self, values):
        indices = []
        for idx, (num, next_num) in enumerate(zip(values, values[1:])):
            if num == next_num:
                indices.append(idx)
        return indices

    def delete(self, values, repeated_idx):
        empty_frequencies = sorted(list(set([i for i in range(values[-1] + 1)]).difference(set(values))), reverse=True)
        delete_counter = 0
        # print(empty_frequencies)
        for idx in repeated_idx:
            # val = values[idx]
            for emp_idx, empty_value in enumerate(empty_frequencies):
                if empty_value < values[idx]:
                    delete_counter += (values[idx] - empty_value)
                    if empty_value != 0:
                        empty_frequencies = empty_frequencies[:emp_idx] + empty_frequencies[emp_idx+1:]
                    break
        return delete_counter


if __name__ == '__main__':
    s = Solution()

    inp = 'abbbbb'
    print(s.minDeletions(inp))