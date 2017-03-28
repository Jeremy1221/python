#!/usr/bin/python
# -*- coding:UTF-8 -*-

l = []
for i in xrange(0,3):
	x = int(raw_input('integer:\n'))
	l.append(x)
l.sort()
print l
l.sort(reverse = True) #逆序
print l