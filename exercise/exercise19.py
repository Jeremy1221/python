#!/usr/bin/python
# -*- coding:UTF-8 -*-

from sys import stdout
for i in xrange(2,1001):
	k = []
	n = -1
	s = i
	for j in xrange(1,i):
		if i % j == 0:
			n += 1
			s -= j
			k.append(j)
	if s == 0:
		print i
		for j in xrange(n):
			stdout.write(str(k[j]))
			stdout.write(' ')
		print k[n]