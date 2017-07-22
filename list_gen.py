#coding=utf-8
g=(x for x in [1,2,3,4,5,6,7,8])
print(g)
print(next(g))
print(help(next))
#next可以读取迭代中的下一个数值，有限的话会直到结束并报错
for i in g:
	print(i)
#正确的是用循环进行有限迭代的输出。
print('\n')

def fib(max):
	n, a, b = 0, 0, 1
	while n < max:
		print(b)
		a, b = b, a + b
		n = n + 1
	return 'done'
fib(6)
print('\n')

def fib(max):
	n, a, b = 0, 0, 1
	print("chaojidashabi")
	while n < max:
		yield b
		a, b = b, a + b
		n = n + 1
	return print('done')
for i in fib(5):
	print(i)


print("____________________")
#这两者区别就是第一个打印出了b的值
#后者成为了一个生成器，并且每次执行时只在yield所在循环

# 练习
#
# 杨辉三角定义如下：
#
#           1
#         1   1
#       1   2   1
#     1   3   3   1
#   1   4   6   4   1
# 1   5   10  10  5   1
# 把每一行看做一个list，试写一个generator，不断输出下一行的list：

# -*- coding: utf-8 -*-

def triangles(nl):
	l1 = []
	for i in range(1,nl+1):
		l2=[]
		for m in range(1,i+1):
			if m==1:
				l2.append(1)
			elif m<i:
				l2.append(l1[m-2]+l1[m-1])
			else:
				l2.append(1)
		l1=l2
		print(l2)
triangles(6)

def triangles():
	L = [1]
	while True:
		yield L
		L.append(0)
		L = [L[i - 1] + L[i] for i in range(len(L))]
#这里每个数的值是上一行同一个位置的值与上一行前一个位置值的和，因为新一行比旧的一行少一位，所以提前补足一位数值0
#这样第一个数会找上一个数列的最后一位，最后一个数也可找到上一行序号相同的最后一位。
#制作生成器的方式，第二次开始每次运行生成器是从yield开始
n = 0
for t in triangles():
	print(t)
	n = n + 1
	if n == 10:
		break





