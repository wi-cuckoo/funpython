#! /usr/bin/env python
# -*- coding:utf-8 -*-


class Sort(object):

    def __init__(self, method):
        self.method = method

    def do(self, l):
        if hasattr(self, self.method):
            return getattr(self, self.method)(l)
        return None

    def bubble(self, seq):
        l = [x for x in seq]
        n = len(l)
        while n > 0:
            for i in range(0, n-1):
                if l[i] > l[i+1]:
                    l[i], l[i+1] = l[i+1], l[i]
            n -= 1
        return l

    def select(self, l):
        n = len(l)
        seq = [x for x in l]
        while n > 0:
            pos, max_el = 0, seq[0]
            for i in range(1, n):
                if max_el < seq[i]:
                    max_el, pos = seq[i], i
            seq[n-1], seq[pos] = seq[pos], seq[n-1]
            n -= 1
        return seq

    def insert(self, l):
        # copy the l
        seq = [x for x in l]
        n = len(seq)
        for i in range(1, n):
            el = seq[i]
            pos = i
            while pos > 0 and seq[pos-1] > el:
                seq[pos] = seq[pos-1]
                pos -= 1
            seq[pos] = el
        return seq

    def merge(self, l):
        seq = [x for x in l]

        def _merge_sort(s):
            if len(s) <= 1:
                return
            mid = len(s) // 2
            left = s[:mid]
            right = s[mid:]
            _merge_sort(left)
            _merge_sort(right)
            i, j, k = 0, 0, 0
            while i<len(left) and j < len(right):
                if left[i] < right[j]:
                    s[k] = left[i]
                    i += 1
                else:
                    s[k] = right[j]
                    j += 1
                k += 1
            while i < len(left):
                s[k] = left[i]
                i += 1
                k += 1
            while j < len(right):
                s[k] = right[j]
                j += 1
                k += 1

        _merge_sort(seq)
        return seq

    def fast(self, l):
        pass

    def count(self, l, fn=lambda x: x):
        a, b = [], {}
        for x in l:
            val = fn(x)
            if b.get(val):
                b[val].append(x)
            else:
                b[val] = [x]

        for i in range(min(b), max(b) + 1, 1):
            if b.get(i) is None:
                continue
            a += b[i]
        return a

if __name__ == '__main__':
    sample = [200, 140, 130, 109, 105, 80, 70, 60, 10, 4]
    print('Bubble Sort: ', Sort('bubble').do(sample))
    print('Select Sort: ', Sort('select').do(sample))
    print('Insert Sort: ', Sort('insert').do(sample))
    print('Merge Sort: ', Sort('merge').do(sample))
    print('Count Sort: ', Sort('count').do(sample))
