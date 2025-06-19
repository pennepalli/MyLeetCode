#!/usr/bin/python3

import sys

def combinations(iterable, r):
    pool = tuple(iterable)
    n = len(pool)
    if r > n:
        return
    indx = list(range(r))
    yield tuple(pool[i] for i in indx)
    while True:
        for i in reversed(range(r)):
            if indx[i] != i + n - r:
                break
        else:
            return
        indx[i] += 1
        for j in range(i+1, r):
            indx[j] = indx[j-1] + 1
        yield tuple(pool[i] for i in indx)


if __name__ == "__main__":
    x = sys.argv[1].split(',')
    n = int(sys.argv[2])
    for i in combinations(x, n):
        print(i)
