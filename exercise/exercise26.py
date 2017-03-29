#!/usr/bin/python
# -*- coding:UTF-8 -*-

num = 5

def factorial(n):
	if n == 1:
		return 1
	else:
		return n * factorial(n - 1)
print factorial(num)