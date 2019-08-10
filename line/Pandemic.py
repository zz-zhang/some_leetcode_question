import sys
import numpy as np


def floyd(graph):
    v = len(graph)
    for i in range(1, v):
        for j in range(i + 1, v):
            for k in range(1, v):
                dis = min(graph[i][j], graph[i][k] + graph[k][j])
                graph[i][j] = dis
                graph[j][i] = dis
    return graph


def main(lines):
    v, e, x, y = lines[0].split(' ')
    v = int(v)
    e = int(e)
    x = int(x)
    y = int(y)
    init_p = np.array([int(lines[1].split(' ')[index]) for index in range(0, len(lines[1].split(' ')))])
    init_t = np.array([int(lines[2].split(' ')[index]) for index in range(0, len(lines[2].split(' ')))])
    immun = np.array([])

    sort_indeces = np.argsort(init_t)
    init_t = init_t[sort_indeces]
    init_p = init_p[sort_indeces]

    edges = [(int(lines[index].split(' ')[0]), int(lines[index].split(' ')[1])) for index in range(3, len(lines))]

    graph = [[0xffffffff for _ in range(0, v + 1)] for __ in range(0, v + 1)]
    for (p1, p2) in edges:
        graph[p1][p2] = 1
        graph[p2][p1] = 1

    # for line in graph:
    #     print(line)

    graph = floyd(graph)

    # for line in graph[1:]:
    #     print(line[1:])


    while init_t.shape[0] > 0:
        # print(init_p)
        # print(init_t)
        time = init_t[0]
        # person = init_p[0]
        # init_t = init_t[1:]
        # init_p = init_p[1:]
        last = False

        if time >= y:
            last = True
            time = y

        tars = []
        mts = []
        for target in range(1, v + 1):
            if target in immun:
                continue
            max_time = -1
            person_index = -1
            for index, person in enumerate(init_p):
                if target not in init_p and graph[person][target] != 0xffffffff:
                    # if time >= graph[person][target]:
                    if init_t[index] + graph[person][target] > max_time:
                        max_time = init_t[index] + graph[person][target]
                        person_index = index
            if max_time != -1:
                tars.append(target)
                mts.append(max_time)
        # print(tars, mts)
        for (target, max_time) in zip(tars, mts):
            init_p = np.append(init_p, target)
            init_t = np.append(init_t, max_time)


        sort_indeces = np.argsort(init_t)
        init_t = init_t[sort_indeces]
        init_p = init_p[sort_indeces]

        # print(init_t)

        if init_t[0] < y:
            last = False
        r_time = min(y, init_t[0])
        y -= r_time
        immun = np.append(immun, init_p[0])
        init_t -= r_time
        if 0 in init_t:
            init_t = init_t[1:]
            init_p = init_p[1:]

        # print(init_p)
        # print(init_t, y)
        # print('_______________')
        if last:
            return init_p.shape[0]


    return 0

if __name__ == '__main__':
#     lines = [
#         '10 17 3 17',
# '1 2 4',
# '12 17 6',
# '10 3',
# '10 1',
# '5 1',
# '10 8',
# '7 2',
# '6 5',
# '2 1',
# '1 4',
# '9 1',
# '4 8',
# '1 7',
# '9 8',
# '7 3',
# '3 4',
# '2 8',
# '9 4',
# '4 7',
#
#     ]
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    result = main(lines)
    print(result)
