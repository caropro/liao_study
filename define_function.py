#coding=utf-8
def my_abs(x):
	if x>=0:
		return x
	else:
		return -x
print(my_abs(13))
print(my_abs(-53))
#自定义绝对值函数


def no():
	pass
#空函数
a=10
if a==10:
	pass
#占位跳过

#参数检查，自定义参数不像内置函数那样出错会进行具体的报错
a=10
print(isinstance(a,(int,float)))
print(help(isinstance))

def my_abs(x):
	if not isinstance(x,(int,float)):
		pass
		raise TypeError("input data type error")
	#当类型不符合时，报错内容是typeerror括号内的内容
	if x>=0:
		return x
	else:
		return -x

import math
def move(x,y,length,angle):
	nx=x+length*math.cos(angle)
	ny=y+length*math.sin(angle)
	return nx,ny

x,y=move(0,0,20,math.pi/6)
t=move(0,0,20,math.pi/6)
print(x,y)
print(t)
#多个输入输出，输出值只是一个含有多元素的tuple




# 练习
#
# 请定义一个函数quadratic(a, b, c)，接收3个参数，返回一元二次方程：
#
# ax2 + bx + c = 0
#
# 的两个解。
#
# 提示：计算平方根可以调用math.sqrt()函数：

import math
def quadratic(a,b,c):
	x1=(-b+math.sqrt((b**2)-4*a*c))/(2*a)
	x2=	(-b-math.sqrt((b**2)-4*a*c))/(2*a)
	return x1,x2

print(quadratic(2, 3, 1))
#二次方程求解