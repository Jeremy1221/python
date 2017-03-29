#!/usr/bin/python
# -*- coding:UTF-8 -*-

up = 2.0
down = 1.0
s = 0
arr = []

for i in xrange(20):
	s += up/down
	arr.append(up/down)
	temp = up + down
	down = up
	up = temp
print s
print reduce(lambda x, y : x + y, arr)