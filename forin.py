#coding=utf-8
a=[1,2,3,4,5]
for x in a:
	print(x)
#循环for循环是顺序循环

sum=0
for x in range(101):
	print(x)
	sum+=x
print(sum)
#range取值不包含最后的数值，这里是0-101,不含101

n=0
sum=0
while n<100:
	sum+=n
	n+=2
	print(n,"\n",sum)
#while循环是条件循环，满足条件就可运行

# 练习
#
# 请利用循环依次对list中的每个名字打印出Hello, xxx!：

# -*- coding: utf-8 -*-
L = ['Bart', 'Lisa', 'Adam']
for a in L:
	print("Hello,",a,"!")


