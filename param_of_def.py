#coding=utf-8
def power(x):
	x=x*x
	return x
print(power(4))
#自定义平方函数

def power(x,n):
	sum=1
	while n>0:
		n=n-1
		sum*=x
	return sum
print(power(2,3))
print(power(3,4))
#自定义幂函数

def power(x,n=2):
	sum=1
	while n>0:
		n=n-1
		sum*=x
	return sum
print(power(2))
print(power(3,4))
#设置默认值，n=2
infolist={}

def enroll(name,gender,age,city):
	print('name:', name)
	print('gender:', gender)
	print('age:', age)
	print('city:', city)
	infolist[name]=(gender,age,city)

enroll('Adam', 'M',6,'Tianjin')
enroll(city="Tangshan",name='David',age=18,gender='Female')
print(infolist)
#当多个变量输入时，不按顺序的话要用变量名

def li(l=[]):
	#if l is None:
	#	l=[]
	l.append("end")
	return l
print(li([1]))
print(li([]))
print(li())
print(li())
print(li([]))
#默认值在多次执行会被替换掉，因为是变量
def li(l=None):
	if l is None:
		l=[]
	print(l)
	l.append("end")
	return l
#用None这种空的变量来定义，可以保证默认值不被改变。

def calc(*numbers):
	sum = 0
	for n in numbers:
		sum = sum + n * n
	return sum
print(calc(1,2,3,4,5,6))
list=[1,2,3,4,5,6]
print(calc(*list))
#添加*可以将变量变成可变参数，可以一个参数，可以一堆参数,当使用tuple或者数组时用*读取

def person(name, age, **kw):
	print('name:', name, 'age:', age, 'other:', kw)
#*可以套可变参数，**可以套一堆带可变参数的变量，kw=keyword关键字参数
person('a','b',a='c',b='d',c='e',d='f',e='g',f='h')
person('Adam', 45, gender='M', job='Engineer')
person('Nancy','25',city="Newyork")
#而对应的除了赋值的变量
detail={"city":"Mosco"}
person('Danny','19',**detail)
#也可以是有对应值的字典。


def person(name, age, **kw):
	if 'city' in kw:
# 有city参数
		pass
	if 'job' in kw:
# 有job参数
		pass
	print('name:', name, 'age:', age, 'other:', kw)
person("Anna",13,code=12345)
person('Jack', 24, city='Beijing', addr='Chaoyang', zipcode=123456)
person('Jack', 24, city='Beijing', job='Engineer')
#可以检查可变参数中有没有关键字变量，虽然这里的没卵用

def person(name, age, *, city, job):
	print(name, age, city, job)
person('Jack', 24, city='Beijing', job='Engineer')
person('Jack',24,  job='Cook', city='Shanghai')
#星号后面的是关键字变量，名称不能瞎改,位置可以变,但位置变量不能换

def person(name, age, *args, city, job):
	print(name, age, args, city, job)
person('Jack', 24,2223,2399,city='Beijing', job='Engineer')
#*args前的会按照位置对应，之后的要按照变量名称对应参数，中间的扔到tuple中。
#这种适合于那些多个输入变量，并且有一部分变量拥有默认数值的


def fx(a,b,c=0,*args,d,**kw):
	print(a,b,c,args,d,kw)
#这里a，b是位置参数，c是默认参数，*arg是可变参数，d是命名关键字参数，kw是关键字参数
fx(1,2,3,4,5,d=6,e=7,f=8)

li=(1,2,3,4,5)
pi={'d':12,'e':23}
fx(*li,**pi)
#一个*是可变参数，读的tuple。两个*是可变关键字参数，读dict。





