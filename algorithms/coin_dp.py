#! /usr/bin/env python3
# -*- coding:utf-8 -*-

COINS = [1, 3, 5]
MAX = 20

def coins():
	DP = [float('inf')] * MAX
	DP[0] = 0
	for i in xrange(MAX):
		for c in COINS:
			if i >= c and DP[i-c]+1 < DP[i]:
				DP[i] = DP[i-c] + 1
	return DP

if __name__ == '__main__':
	print coins()