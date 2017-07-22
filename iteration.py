#coding=utf-8
l=(1,2,3,4,5,6,7,8,9)
for i in l:
	print(i)

l2={'a':1,'b':2,'c':3}
for i in l2:
	print(i)
#字典也可以迭代
for i in l2.values():
	print(i)
#可以直接循环数值
for i in l2.keys():
	print(i)
#可以直接循环关键字
for i,m in l2.items():
	print(i,m)
#可以用item来读关键字和数值
print('\n')

from collections import Iterable
isinstance('abc', Iterable) # str是否可迭代
isinstance([1,2,3], Iterable) # list是否可迭代
isinstance(123, Iterable) # 整数是否可迭代

for i,v in enumerate((1,2,3,4,5,6)):
	print(i,v)
#enumerate可以将list或tuple进行序号处理，从0开始计数
print('\n')

for i,v in [(1,2),(3,4),(5,6)]:
	print(i,v)
#循环对数也可以

print('\n')

for i in [(1,2),(3,4),(5,6)]:
	print(i)
	a = ''
	for v in i:
		v=str(v)
		a=a+' '+v
	print(a)




