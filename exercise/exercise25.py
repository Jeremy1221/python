#!/usr/bin/python
# -*- coding:UTF-8 -*-

sum = 0
t = 1
for i in xrange(1,21):
	t *= i
	sum += t
print sum

s = 0
l = range(1, 21)
def op(x):
	r = 1
	for i in xrange(1,x + 1):
		r *= i
	return r
s = sum(map(op, l))
print '1! + 2! + 3! + ... + 20! = %d' % s