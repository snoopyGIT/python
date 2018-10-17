#!/usr/bin/env python
#coding=utf-8

from collections import Iterable
from collections import Iterator
import os

print('切片：列表、元祖、字符串等')
#切片
tlist = list(range(100));
#取0到3
print(tlist[0:3])
#取前5个
print(tlist[:5])
#取倒数第10到倒数第5
print(tlist[-10:-5])
#取前20个数，每两个取一个
print(tlist[:20:2])
#元祖切片
print((0, 1, 2, 3)[:2])
#字符串切片
print('ABCDE'[:3])

print('可作用于所有可迭代的对象上')
tlist = [1, 2]
ttuple = (1, 2)
tdict = {'a':1, 'b':2}
tstr = '12'
for k in tlist:
	print(k)
for k in ttuple:
	print(k)
for k in tdict:
	print(tdict[k])
for k in tstr:
	print(k)
print('对象可迭代判断')
print('abc可迭代：', isinstance('abc', Iterable))
print('123可迭代：', isinstance(123, Iterable))

#enumerate函数可以把一个list变成索引-元素对
print('enumerate函数可以把一个list变成索引-元素对')
for i, v in enumerate(['a', 'b']):
	print(i, v)
for name, age in [('rain', 18), ('snoopy', 8)]:
	print(name, age)

print('列表生成式')
print([x * x for x in range(1, 11)])
print([x * x for x in range(1, 11) if x % 2 == 0])
print([m + n for m in '123' for n in 'abc'])
print([d for d in os.listdir('.')])
d = {'a' : '1', 'b' : '2'}
print([k + '=' + v for k, v in d.items()])
print([s.lower() for s in ['Hello', 'World', 'IBM', 'Apple']])


print('生成器generator()')
print('列表：', [x * x for x in range(10)])
print('生成器：', (x * x for x in range(10)))
print('包含yield关键字的函数也是一个generator')
def fib(max):
	n, a, b = 0, 0, 1
	while n < max:
		yield b
		a, b = b, a + b
		n = n + 1
	return 'done'
print(fib(6))
print('获取generator的return语句的返回值')
g = fib(6)
while True:
	try:
		x = next(g)
		print('g:', x)
	except StopIteration as e:
		print('Generator return value:', e.value)
		break
print('杨辉三角generator:')
def triangles():
	n, ret = 1, [1]
	while True:
		yield ret
		ret = [1] + [ret[i] + ret[i+1] for i in range(len(ret) - 1)] + [1]

triangleOne = triangles()
n = 0;
results = []
for t in triangleOne:
	results.append(t)
	n = n + 1
	if n == 10:
		break
if results == [
    [1],
    [1, 1],
    [1, 2, 1],
    [1, 3, 3, 1],
    [1, 4, 6, 4, 1],
    [1, 5, 10, 10, 5, 1],
    [1, 6, 15, 20, 15, 6, 1],
    [1, 7, 21, 35, 35, 21, 7, 1],
    [1, 8, 28, 56, 70, 56, 28, 8, 1],
    [1, 9, 36, 84, 126, 126, 84, 36, 9, 1]
]:
    print('测试通过!')
else:
    print('测试失败!')

print('迭代器')
print('可以被next()函数调用并不断返回下一个值的对象称为迭代器：Iterator。')
print('生成器都是Iterator对象，但list、dict、str虽然是Iterable，却不是Iterator。')
print('把list、dict、str等Iterable变成Iterator可以使用iter()函数')
print(isinstance(iter([]), Iterator))