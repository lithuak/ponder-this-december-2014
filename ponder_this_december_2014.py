# -*- coding: utf-8 -*-
from collections import Counter
import numpy as np


def int2bin(i, align):
    b = [int(x) for x in bin(i)[2:]]
    return [0] * (align - len(b)) + b


def go(N, M):
    t = Counter()
    eg = {}
    nbits = N * M
    for i in range(0, 1 << nbits):
        b = int2bin(i, nbits)
        a = np.asarray(b).reshape(N, M)
        nsum = np.sum(a, 0)
        msum = np.sum(a, 1)
        key = (tuple(msum), tuple(nsum))
        t[key] += 1
        eg[key] = a
    return t, eg



