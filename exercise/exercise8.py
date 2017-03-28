#!/usr/bin/python
# -*- coding:UTF-8 -*-

for i in xrange(1,10):
	print
	for j in xrange(1,i + 1):
		print '%d * %d = %d' % (i, j, i * j),