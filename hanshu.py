#coding=utf-8
a=-18
print(a)
a=abs(a)
print(a)
#abs绝对值

a=max(1,2,3,4,5,0,-14)
print(a)
#求最大值

a=1
print(a)
print(type(a))

a=float(a)
print(a)
print(type(a))

a=str(a)
print(a)
print(type(a))

a=bool(a)
print(a)
print(type(a))

a=""
a=bool(a)
print(a)
print(type(a))
#数据类型转换
print("\n")

a=abs
print(a)
print(type(a))
print(a(-19))
#可以指定函数

# 练习
#
# 请利用Python内置的hex()函数把一个整数转换成十六进制表示的字符串：
# -*- coding: utf-8 -*-

n1 = 255
n2 = 1000
print(hex(n1))
print(hex(n2))

print("\n")
help(hex)
#hex将整型转为十六进制