#!/usr/bin/python
# -*- coding:UTF-8 -*-

tour = []
height = []

h = 100.0
up = 0.0
down = 100.0
tim = 10

for i in xrange(tim):
	tour.append(up + down)
	h /= 2
	height.append(h)
	up = h
	down = h
print('总高度： tour = {0}'.format(sum(tour)))
print('第10次反弹高度：height = {0}'.format(h))
#100+100+50+25+12.5+6.25+3.125+1.5625+0.78125+0.390625+0.1953125+0.09765625
#299.609375
#0.1953125