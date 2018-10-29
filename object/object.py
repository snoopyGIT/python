#!/usr/bin/env python
#coding=utf-8

class Student(object):
	"""学生类"""
	def __init__(self, name, score):
		super(Student, self).__init__()
		self.__name = name
		self.__score = score
		
	def print_score(self):
		print('%s: %s' % (self.__name, self.__score))

	def get_grade(self):
		if self.__score >= 90:
			return 'A'
		elif self.__score >= 60:
			return 'B'
		else:
			return 'C'

print('类与私有变量')
snoopy = Student('Snoopy', 100)
snoopy.print_score()
print(snoopy.get_grade())


class Animal():
	"""Animal类"""
	def run(self):
		print('Animal is running...')
		
print('继承和多态')
print('继承')
class Dog(Animal):
	"""Dog类"""
	def eat(self):
		print('Eating meat...')

class Cat(Animal):
	"""Cat类"""
	def __init__(self, name):
		super(Cat, self).__init__()
		self.name = name
	def run(self):
		print('Cat is running')
	def eat(self):
		print('Eating meat...')

def run_twice(animal):
	animal.run()
	animal.run()

animals = []
dog = Dog()
animals.append(dog)
dog.run()
dog.eat()
print('多态')
cat = Cat('Kitty')
animals.append(cat)
cat.run()
cat.eat()

for x in animals:
	run_twice(x)

print('获取对象信息')
print(type(cat))
print(dir(cat))

print('配合getattr()、setattr()以及hasattr()')
if hasattr(cat, 'run'):
	fn = getattr(cat, 'run')
	fn()

class Test():
	"""docstring for Test"""
	count = 0
	def __init__(self, name):
		self.name = name
		Test.count += 1

test = Test('1')
print(test.count)
test = Test('1')
print(test.count)
test = Test('1')
print(test.count)
		