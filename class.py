#coding=utf-8
# class student(object):
# 	pass
#
# bart=student()
# print(bart)
# print(student)
#
# bart.name="billy jim"
# print(bart.name)

#
# class student():
#
# 	def __init__(self,name,score):
# 		self.name=name
# 		self.score=score
#
# bart=student("halo",23)
# print(bart)
# print(bart.name)
# print(bart.score)
#
# def prints_core(std):
# 	print("%s : %s" % (std.name,std.score))
#
# prints_core(bart)

# class student(object):
# 	def __init__(self,name,score):
# 		self.name=name
# 		self.score=score
#
# 	def print_score(self):
# 		print("%s : %s" %(self.name,self.score))
# 	def get_grade(self):
# 		if self.score >= 90:
# 			return 'A'
# 		elif self.score >= 60:
# 			return 'B'
# 		else:
# 			return 'C'
#
# bart=student("james",98)
# bart.print_score()
# print(bart.get_grade())
#
# class student(object):
# 	def __init__(self,name,score):
# 		self.__name=name
# 		self.__score=score
#
# 	def print(self):
# 		print("%s:%s" % (self.__name,self.__score))
# 	def get_name(self):
# 		return self.__name
# 	def get_score(self):
# 		return self.__score
# 	def set_name(self,name):
# 		self.__name=name
# 	def set_score(self,score):
# 		if 0<=score<=100:
# 			self.__score=score
# 		else:
# 			print("no")
#
# bart=student("hehe",24)
# bart.print()
#
# print(bart.get_name())
# print(bart.get_score())
#
# bart.set_name("Participate")
# bart.set_score(99)
# bart.print()
#
# bart._student__name=("jjjjjjjj")
# bart.__name=("ffffff")
# print(bart.__name)
# print(bart._student__name)
# print(bart.get_name())
# print(bart.__name)
#
# class Green(object):
# 	def shot(self):
# 		print("waaaaaaah")
# class Org(Green):
# 	def shot(self):
# 		print("Org waaaaaah")
# class Boyz(Green):
# 	def shot(self):
# 		print("Boyz waaaaah")
#
# a=Org()
# b=Boyz()
#
# a.shot()
# b.shot()

# class myd(object):
# 	def __len__(self):
# 		return 100
#
# obj=myd()
# print(len(obj))
# print(len("abs"))


# class MyObject(object):
# 	def __init__(self):
# 		self.x = 9
# 	def power(self):
# 		return self.x * self.x
#
#
#
# obj=MyObject()
# print(hasattr(obj,"x"))
# print(obj.x)

#
# class asbw(object):
# 	def __init__(self):
# 		self.x=999
# class wwert(object):
# 	def __init__(self):
# 		self.x = 999
# 	def pow(self):
# 		return self.x*self.x
# a=wwert()
# print(a.x)
# b=getattr(a,"pow")
# print(b())



class ina(object):
	name = "haha"

print(ina.name)
a=ina()
a.name="bububu"
print(a.name)
delattr(a,"name")
print(a.name)
