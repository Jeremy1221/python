#!/usr/bin/python
# -*- coding:UTF-8 -*-

import datetime

if __name__ == '__main__':		#当被直接运行时为True，被import时为false
	#输出今日日期，格式为dd/mm/yy。更多选项可以查看strftime()方法
	print(datetime.date.today().strftime('%d/%m/%Y'))

	#创建日期对象
	miyazakiBirthDate = datetime.date(1941, 1, 5)

	print(miyazakiBirthDate.strftime('%d/%m/%Y'))

	#日期算术运算
	miyazakiBirthNextDay = miyazakiBirthDate + datetime.timedelta(days = 1)

	print(miyazakiBirthNextDay.strftime('%d/%m/%Y'))

	#日期替换
	miyazakiFirstBirthday = miyazakiBirthDate.replace(year=miyazakiBirthDate.year + 1)

	print(miyazakiFirstBirthday.strftime('%d/%m/%Y'))