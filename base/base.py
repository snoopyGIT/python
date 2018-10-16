#!/usr/bin/env python
#coding=utf-8
import sys
print(sys.stdout.encoding)

a = 100
if a >= 0:
	print(a, '大于0')
else:
	print(a, '小于0')


print('多行字符串\n')
print('''第一行
第二行
第三行''')