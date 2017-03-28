#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
def fib(n):
	a, b = 0, 1
	for i in xrange(n - 1):
		a,b = b, a+b
	return a
print fib(4)
'''

'''
#使用递归
def fib(n):
	if n == 0:
		return
	elif n == 1:
		return 0
	elif n == 2:
		return 1
	else:
		return fib(n - 1) + fib(n - 2)
print fib(10)
'''

def fib(n):
	fibs = [0, 1]
	if n == 0:
		return
	elif n == 1:
		return [0]
	elif n == 2:
		return [0, 1]
	else:
		for i in xrange(2,n):
			a = fibs[-1]
			b =  fibs[-2]
			fibs.append(a + b)

	return fibs
print fib(1)
