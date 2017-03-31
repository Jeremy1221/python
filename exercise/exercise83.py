#!/usr/bin/python
# -*- coding:UTF-8 -*-

if __name__ == '__main__':
	sum = 4
	s = 4
	for i in xrange(2,9):
		print sum
		if i <= 2:
			s *= 7
		else:
			s *= 8
		sum+=s
	print 'sum = %d' % sum