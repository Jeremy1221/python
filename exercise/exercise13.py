#!/usr/bin/python
# -*- coding:UTF-8 -*-

for i in xrange(100,1000):
	t = i / 100
	h = (i / 10) % 10
	g = i % 10
	total = t*t*t + h*h*h + g*g*g
	if total == i:
		print i