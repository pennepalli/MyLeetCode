#!/usr/bin/python3

import sys

def fast_pow(x, n):
    if n == 0:
        return 1.0
    half = fast_pow(x, n // 2)
    if n % 2 == 0:
        return half * half
    else:
        return half * half * x

    if n < 0:
        return 1 / fast_pow(x, -n)
    else:
        return fast_pow(x, n)

if __name__ == "__main__":
    base = float(sys.argv[1])
    pow = float(sys.argv[2])
    n = fast_pow(base,pow)
    print(n)
