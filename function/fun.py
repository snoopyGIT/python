#!/usr/bin/env python
#coding=utf-8

import math

def move(x, y, step, angle=0):
	nx = x + step * math.cos(angle)
	ny = y + step * math.sin(angle)
	return nx, ny

#一元二次方程求解
def x2result(a, b, c):
	dt = math.pow(b, 2) - 4*a*c
	if dt >= 0:
		return (-b + math.pow(dt, 0.5)) / 2 / a, (-b - math.pow(dt, 0.5)) / 2 / a
	else:
		raise EOFError('bad input')

#n次方函数
def power(x, n=2):
	s = 1
	while n > 0:
		n = n -1
		s = s * x
	return s

#求和(可变参数)
def calc(*numbers):
	sum = 0
	for n in numbers:
		sum += n
	return sum

#用户(关键字参数)
def person(name, age, **kw):
	print('name:', name, 'age:', age, 'other:', kw)
	if 'job' in kw:
		print(name, 'has a job')

#用户(命名关键字参数，调用的时候必须传入关键字参数)
def person2(name, age, *, city, job):
	print('name:', name, 'age:', age, 'other:', kw)
	if 'job' in kw:
		print(name, 'has a job')

#用户(命名关键字参数，前面已经有可变参数，调用的时候必须传入关键字参数)
def person3(name, age, *args, city, job):
	print('name:', name, 'age:', age, 'other:', kw)
	if 'job' in kw:
		print(name, 'has a job')

#阶乘(递归函数)
def fact(n):
	if n == 1:
		return 1
	return n * fact(n - 1)

x, y = move(0, 100, 60, math.pi / 6)
print(x, y)

x1, x2 = x2result(1, 3, 1)
print(x1, x2)
print(power(5))
print(power(5, 3))


print(calc(1, 2, 3))
nums = [1, 2, 3]
print(calc(*nums))

person('Rain', 20, city='GZ')
person('Bob', 30, city='BJ', job='teacher')
extra = {'city': 'GZ', 'job': 'Engineer'}
person('Snoopy', 28, **extra)

#参数定义的顺序必须是：必选参数、默认参数、可变参数、命名关键字参数和关键字参数
print('小结：', '参数定义的顺序必须是：必选参数、默认参数、可变参数、命名关键字参数和关键字参数')


print(fact(5))