#!/usr/bin/python
# -*- coding:UTF-8 -*-

if __name__ == '__main__':
	import time
	import random

	play_it = raw_input('do you want to play it?(\'y\' or \'n\'\n)')
	while play_it == 'y':
		c = raw_input('input a character:\n')
		i = random.randint(0, 2**32) % 100       #2**32 = 2的32次方
		print 'please input number you guess:\n'
		start = time.clock()
		a = time.time()
		guess = int(raw_input('input your guess:\n'))
		while  guess != i:
			if guess > i:
				print 'Please input a little smaller'
				guess = int(raw_input('input your guess:\n'))
			else:
				print 'Please input a little bigger'
				guess = int(raw_input('input your guess'))
			
		end = time.clock()
		b = time.time()
		var = (end - start) / 18.2
		print var
		#pint 'It took you %6.3 seconds' % time.difftime(b, a)
		if var < 15:
			print 'you are very clever!'
		elif var < 25:
			print 'you are normal'
		else:
			print 'you are stupid'
		print 'Congradulations'
		print 'The number you guess is %d' % i
		play_it = raw_input('do you want to play it?')