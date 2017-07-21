#coding=utf-8
# class bird(object):
# 	def __init__(self,name):
# 		self.name=name
# 	def __str__(self):
# 		return("print name of %s" % self.name)
# 	__repr__=__str__
# a=bird("swift")
# print(a.name)
# print(a)


# class addd(object):
# 	def __init__(self):
# 		self.a,self.s=1,1
# 	def __iter__(self):
# 		return self
# 	def __next__(self):
# 		self.a+=1
# 		self.s+=self.a
# 		if self.a>100:
# 			raise StopIteration
# 		return self.s
#
# for a in addd():
# 	print(a)

# a=['asdaasdads']
# print(a[1:3:1])
# a=slice(1,10,1)
# print(a)
# print(isinstance(a,slice))

# class ru(object):
# 	def __getitem__(self, n):
# 		a=1
# 		for i in range(n):
# 			a=a+1
# 		return a
# f=ru()
# print(f[5])
#
# class sl(object):
# 	def __getitem__(self, num):
# 		if isinstance(num,int):
# 			a=1
# 			for i in range(num):
# 				a=a+1
# 			return a
# 		if isinstance(num,slice):
# 			st=num.start
# 			sp=num.stop
# 			if st==None:
# 				st=0
# 			a=1
# 			l=[]
# 			for i in range(sp):
# 				a+=1
# 				if i> st:
# 					l.append(a)
# 			return l
#
# a=sl()
# print(a[4])
# print(a[:10])

# class name(object):
# 	def __init__(self,num):
# 		self.num=num
# 	def __call__(self):
# 		print("the nummber is : %s" % self.num)
#
# a=name("123123123")
# a()

# from enum import Enum
#
# Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))
#
# for name, member in Month.__members__.items():
#     print(name, '=>', member, ',', member.value)
#
# a='basd'
# print(a)
#
# b=a[0]
# c=a[1:-1]
# print(b)
# print(c)
# a=c+b+"py"
# print(a)
#
# class Listmetaclass(type):
# 	def __new__(cls,name,bases,attrs):
# 		attrs['add']=lambda self,value:self.append(value)
# 		return type.__new__(cls,name,bases,attrs)
#
# class Mylist(list,metaclass=Listmetaclass):
# 	pass
#
# L=Mylist([2,3,4])
# L.add(1)
# print(L)
#
# a=(1,2,{"a":"b"})
# print(a,type(a))
# b=a[2]
# print(b,type(b))


# class te(object):
# 	pass
#
# a=type("hehe",(te,),{"pi":15})
# print(a.pi)
# print(type(a))
# print(a())
# print(a().pi)
# print(type(a().__class__))

