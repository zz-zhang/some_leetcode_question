# https://atcoder.jp/contests/exawizards2019/tasks/exawizards2019_c

def main(n, q, s, t, d):
    human = [1 for _ in range(n)]
    w_map = {}
    for (i, c) in enumerate(s):
        if c not in w_map:
            w_map[c] = [i]
        else:
            w_map[c].append(i)

    for index in range(q):
        temp_human = [item for item in human]
        if t[index] in w_map:
            if d[index] == 'L':
                for loc in w_map[t[index]]:
                    if loc != 0:
                        temp_human[loc - 1] += human[loc]
                    temp_human[loc] = 0
            else:
                for loc in w_map[t[index]][::-1]:
                    if loc != n - 1:
                        temp_human[loc + 1] += human[loc]
                    temp_human[loc] = 0
            human = [item for item in temp_human]
        # print(human)
    return sum(human)

if __name__ == '__main__':
    input_line = input()
    n, q = input_line.split(' ')
    n = int(n)
    q = int(q)
    s = input()
    t, d, = [], []
    for _ in range(q):
        input_line = input()
        temp_t, temp_d = input_line.split(' ')
        t.append(temp_t)
        d.append(temp_d)
    # print(list(s))
    print(main(n, q, s, t, d))