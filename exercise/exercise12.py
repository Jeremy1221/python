#!/usr/bin/python
# -*- coding:UTF-8 -*-

from math import sqrt
from sys import stdout
count = 0
leap = 1
for i in xrange(101,201):
	temp = int(sqrt(i))
	print '%d, %d' % (i, temp + 1)
	for j in xrange(2,temp + 1):
		if i % j == 0:
			leap = 0
			break
	if leap == 1:
		#print '%-4d' % i
		count+=1
	leap = 1
print count