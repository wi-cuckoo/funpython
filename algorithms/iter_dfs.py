#! /usr/bin/env python
# -*- coding:utf-8 -*-


def example():
    a, b, c, d, e, f, g, h = range(8)
    N = [
        {b: 2, c: 1, d: 3, e: 9, f: 4},
        {c: 4, e: 3},
        {d: 8},
        {e: 7},
        {f: 5},
        {c: 2, g: 2, h: 2},
        {f: 1, h: 6},
        {f: 9, g: 8}
    ]

    return N


def iter_dfs(G, s):
    S, Q = set(), []
    Q.append(s)
    while Q:
        u = Q.pop()
        if u in S: continue
        S.add(u)
        Q.extend(G[u])
        yield u

if __name__ == '__main__':
    G = example()
    for i in iter_dfs(G, 0):
        print i,
