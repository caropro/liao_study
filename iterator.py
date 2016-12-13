#coding=utf-8
from collections import *
print (isinstance([],Iterable))
print (isinstance({},Iterable))
print (isinstance((),Iterable))
print(isinstance([x for x in range(10)],Iterable))
#判断可不可以迭代
print (isinstance([],Iterator))
print (isinstance({},Iterator))
print (isinstance((),Iterator))
print (isinstance([x for x in range(10)],Iterator))
#判断是不是迭代器
print(isinstance(iter([]),Iterator))
print(isinstance(iter([x for x in range(10)]),Iterator))
#iter可以将可迭代转为迭代器

def t(x):
	while x>0:
		a=x-1
		yield a
		x = x - 1
for i in t(10):
	print(i)

g=t(8)
print(isinstance(g,Iterator))