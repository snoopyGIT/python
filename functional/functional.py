#!/usr/bin/env python
#coding=utf-8
from functools import reduce
import functools
import time

#高价函数
def add(x, y, f=None):
	if f==None:
		return x + y
	else:
		return f(x) + f(y)

def fn(x, y):
	return abs(x) * 10 + abs(y)

DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
def str2int(s):
    def fn(x, y):
        return x * 10 + y
    def char2num(s):
        return DIGITS[s]
    return reduce(fn, map(char2num, s))

def is_odd(n):
	return n % 2 == 1

print('绝对值加法add(-5, -2, abs)：', add(-5, -2, abs))

print('map()和reduce()函数')
print('map将传入的函数依次作用到序列的每个元素，并把结果作为新的Iterator返回')
print(list(map(abs, [-1, 2, 4, -10])))

print('reduce把一个函数作用在一个序列[x1, x2, x3, ...]上，这个函数必须接收两个参数，reduce把结果继续和序列的下一个元素做累积计算')
print(reduce(add, [1, 2, 3, 4, 5, 1]))
print(reduce(fn, [2, 0, 1, 8]))
print('str2int:', str2int('6534'))

print('filter()把传入的函数依次作用于每个元素，然后根据返回值是True还是False决定保留还是丢弃该元素')
print(list(filter(is_odd, [1, 2, 4, 5, 6, 9, 10, 15])))

#sorted()函数也是一个高阶函数，它还可以接收一个key函数来实现自定义的排序
print('sorted()函数也是一个高阶函数，它还可以接收一个key函数来实现自定义的排序')
print(sorted([1, -1, 2, -3, 10, -22]))
print(sorted([1, -1, 2, -3, 10, -22], key=abs))
print(sorted(['bob', 'about', 'Zoo', 'Credit']))
print(sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower))
print(sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower, reverse=True))


#函数作为返回值
print('函数作为返回值')
def lazy_sum(*arg):
	def sum():
		ax = 0
		for x in arg:
			ax = ax + x
		return ax
	return sum
f = lazy_sum(2, 4, 6, 8)
print(f)
print(f())

def createCounter():
	c = [0]
	def counter():
		c[0] += 1
		return c[0]
	return counter

c = createCounter()
print(c())
print(c())
print(c())

#匿名函数
print('匿名函数')
print(list(map(lambda x: x * x, [1, 2, 3, 4, 5])))
print(list(filter(lambda x: x % 2 == 1, range(1, 20))))

#在代码运行期间动态增加功能的方式，称之为“装饰器”（Decorator）
print('在代码运行期间动态增加功能的方式，称之为“装饰器”（Decorator）')
def log(func):
	@functools.wraps(func)
	def wrapper(*arg, **kw):
		print('call %s()' % func.__name__)
		return func(*arg, **kw)
	return wrapper

#decorator本身需要传入参数，那就需要编写一个返回decorator的高阶函数
print('decorator本身需要传入参数，那就需要编写一个返回decorator的高阶函数')
def log2(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator

@log
def now():
	print('2018-10-17')

@log2('执行')
def halo():
	print('你好')

now()
print(now.__name__)
halo()
print(halo.__name__)

def run_time(func):
	@functools.wraps(func)
	def wrapper(*arg, **kw):
		start_time = time.time()
		f = func(*arg, **kw)
		print('run time:%d%s' % (int(1000 * (time.time() - start_time)), 'ms'))
		return f
	return wrapper

@run_time
def wait():
	print('running......')
	time.sleep(.5)
	print('end......')

wait()

#偏函数functools.partial
print('偏函数functools.partial')
int2 = functools.partial(int, base=2)
print(int2('10101010'))
max2 = functools.partial(max, 10)
print(max2(1, 2, 3, 4))