#coding=utf-8
print(help(map))
#map(func, *iterables) --> map object
#作为一个类，前者是函数，后者是迭代用的变量

def f(x):
	return x**2
a=map(f,[1,2,3,4,5,6])
print(list(a))

print(list(map(str, [1, 2, 3, 4, 5, 6, 7, 8, 9])))
#map用法

from functools import reduce
print(help(reduce))
# reduce(...)
#     reduce(function, sequence[, initial]) -> value
#先输入需要两个变量的函数，后跟序列变量
# reduce(lambda x, y: x+y, [1, 2, 3, 4, 5]) calculates
#     ((((1+2)+3)+4)+5)函数依次嵌套

def a(x,y):
	return (x+1)*y

print(reduce(a,[1,2,3,4,5,6]))


from functools import reduce
def fn(x, y):
	return x * 10 + y
def char2num(s):
	return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]

print(list("abcdefg"))
#list可以将str拆开变成列表的元素
print(reduce(fn, map(char2num, '13579')))


from functools import reduce

def str2int(s):
	def fn(x, y):
		return x * 10 + y
	def char2num(s):
		return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]
	return reduce(fn, map(char2num, s))
#将两个函数放到一个大的函数下，开始以为这个案例说的str to int 是把引号去掉，结果只是单纯连起来那种。

# 练习
#
# 利用map()函数，把用户输入的不规范的英文名字，变为首字母大写，其他小写的规范名字。输入：['adam', 'LISA', 'barT']，输出：['Adam', 'Lisa', 'Bart']：
def normalize(name):
	name=name.capitalize()
	return name
# 测试:
L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print(L2)

# Python提供的sum()函数可以接受一个list并求和，请编写一个prod()函数，可以接受一个list并利用reduce()求积：
# -*- coding: utf-8 -*-

from functools import reduce

def prod(L):
	return reduce(lambda x,y:x*y ,L)

print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))
print(3 * 5 * 7 * 9)

# 利用map和reduce编写一个str2float函数，把字符串'123.456'转换成浮点数123.456：
# -*- coding: utf-8 -*-

from functools import reduce

def str2float(s):
	a=s.split('.')
	f=list(a[0])
	b=list(a[1])
	b.reverse()
	def se(s):
		return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]
	def inf(f):
		sum1=reduce(lambda x,y:x*10+y ,map(se,f))
		return sum1
	def bnf(b):
		sum2=0.1*reduce(lambda x,y:x*0.1+y ,map(se,b))
		return sum2
	sum=inf(f)+bnf(b)
	return sum

print('str2float(\'123.456\') =', str2float('123.456'))
#分成两部分索引，前部分正数后部分小数

def str2float(s):
	x=s.split('.')
	x0=x[0]
	x1=x[1]
	def fun(x,y):
		return x*10 + y
	print(x)
	print(x0)
	print(x1)
	s=reduce(fun, map(int, x0)) + (reduce(fun, map(int, x1))) / 10 ** (len(x1))
	return s

print('str2float(\'123.456\') =', str2float('123.456'))
#别人的，没有了索引省了一段计算。

