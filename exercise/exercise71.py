#!/usr/bin/python
# -*- coding:UTF-8 -*-

N = 3
#num : string
#name : string
#score[4] : list
student = []

for i in xrange(5):
	student.append(['', '', []])

def input_stu(stu):
	for i in xrange(N):
		stu[i][0] = raw_input('input student num:\n')
		stu[i][1] = raw_input('input student name:\n')
		for j in xrange(3):
			stu[i][2].append(int(raw_input('score:\n')))

def output_stu(stu):
	for i in xrange(N):
		print '%-6s%-10s' % (stu[i][0], stu[i][1])
		for j in xrange(3):
			print '%-8d' % stu[i][2][j]

if __name__ == '__main__':
	input_stu(student)
	print student
	output_stu(student)