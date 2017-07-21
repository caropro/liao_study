#coding=utf-8
# class student(object):
# 	pass
#
# s=student()
# s.name="hello"
# print(s.name)
#
# def set_age(self,age):
# 	self.age=age
# from types import MethodType
# s.setage=MethodType(set_age,s)
# s.setage(23)
# print(s.age)


# class student(object):
# 	pass
# a=student()
# a.age=12
# print(a.age)
#
# from types import MethodType
# def setage(self,age):
# 	self.age=age
# student.setage=setage
#
# a.setage(14)
# print(a.age)

# class student(object):
# 	__slots__ = ("gen","age")
# a=student()
# a.gen="male"
# a.age=124
# class aa(student):
# 	pass
# b=aa()
# b.gen="female"
# b.age=24
# b.aaa="ccc"

# class student(object):
# 	def getname(self):
# 		return self.getname
# 	def setname(self,name):
# 		if not isinstance(name,str):
# 			raise ValueError("Not a str name")
# 		if len(name)>10:
# 			raise  ValueError("Too long")
# 		self.name=name
#
# a=student()
# a.setname("gggawga")
# print(a.name)
# a.setname("asdadsasdadsada")
#

# -*- coding: utf-8 -*-

class Screen(object):
	# @property
	# def width(self):
	# 	return self._width
	# @width.setter
	# def width(self,width):
	# 	self._width=width
	# @property
	# def height(self):
	# 	return self._height
	# @height.setter
	# def height(self, height):
	# 	self._height = height
	# @property
	# def resolution(self):
	# 	return self._width*self._height

	def isint(self, px):
		if not isinstance(px, int):
			raise ValueError('px must be an integer!')
		if px < 0:
			raise ValueError('px must be an positive integer!')

	@property
	def width(self):
		return self._width

	@width.setter
	def width(self, value):
		self.isint(value)
		self._width = value

	@property
	def height(self):
		return self._height

	@height.setter
	def height(self, value):
		self.isint(value)
		self._height = value

	@property
	def resolution(self):
		return self._width * self._height
# test:
s = Screen()
s.width = 1024
s.height = 768
print(s.resolution)
assert s.resolution == 786432, '1024 * 768 = %d ?' % s.resolution


