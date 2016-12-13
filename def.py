#coding=utf-8
import math
def area_of_circle(x):
	s=math.pi*pow(x,2)
	return s
a=area_of_circle(3)
print(a)
#求圆面积

def sumfunc(x):
	he=0
	for a in range(x+1):
		he+=a
	return he
a=sumfunc(10)
print(a)
#求和

def n2p1(x):
	sums=0
	for a in range(1,x+1):
		sums+=pow(a,2)+1
	return sums
a=n2p1(1)
print(a)
#求平方加一的和


