#!/usr/bin/python
# -*- coding:UTF-8 -*-

from sys import stdout
for i in xrange(4):
	for j in xrange(2 - i + 1):
		stdout.write(' ')
	for k in xrange(2 * i + 1):
		stdout.write('*')
	print
for i in xrange(3):
	for j in xrange( i + 1):
		stdout.write(' ')
	for k in xrange(4 - 2 * i + 1):
		stdout.write('*')
	print