#coding=utf-8
# for i in iter('abc'):
# 	print (i)
#
# b=iter('abc')
# print(next(b))
# print(next(b))
# print(next(b))
#
# for x in [1, 2, 3, 4, 5]:
# 	pass
#
# print(x)
#
# it=iter([1,2,3,4,5])
# #上下等价
# while True:
# 	try:
# 		a=next(it)
# 	except StopIteration:
# 		break
# print(a)

# def addp(a,b,pow):
# 	s=pow(a)+pow(b)
# 	return s
# def pow(a):
# 	b=a**2
# 	return b
#
# c=addp(1,3,pow)
# print(c)

#
# def chartoint(s):
# 	return {"1":1,"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9,"0":0}[s]
# print(list(map(chartoint,"4124124"))
#
# s="aBC"
# print(s.capitalize())

# a="123.345"
# b=a.split(".")
# print(b)
# c=-len(b[1])
# b=b[0]+b[1]
# print(b)
#
# def chartoint(s):
# 	return {"1":1,"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9,"0":0}[s]
# a=list(map(chartoint,b))
# print(a)



# a="find a defing find ccc"
# for b in a:
# 	if b.startswith("a"):
# 		print(b)
# 	else:
# 		continue

# def empty(s):
# 	return s and s.strip()
# cd=empty("    sdsd")
# print(cd and cd.strip())
# c=list(filter(empty, ['A', '', 'B', None, 'C', '  ']))
# print(c)

#
# def _odd_iter():
#     n = 1
#     while True:
#         n = n + 2
#         yield n
#
# def _not_divisible(n):
#     return lambda x: x % n > 0
# n=4
#
# a="abcdfg"
# print(a[::-1])

# a=["svb",'bcsd','asd233',"1313","42123"]
# print(a)
# print(sorted(a,reverse=True))
#

# def count():
#     def f(j):
#         def g():
#             return j*j
#         return g
#     fs = []
#     for i in range(1, 4):
#         fs.append(f(i)) # f(i)立刻被执行，因此i的当前值被传入f()
#     return fs

# def count():
#     fs = []
#     for i in range(1, 4):
#         def f():
#              return i*i
#         fs.append(f)
#     return fs
# f1, f2, f3 = count()
# print(f1(),f2(),f3())

# def count():
# 	def f(j):
# 		return j*j
# 	fs = []
# 	for i in range(1,4):
# 		fs.append(f(i))
# 	return fs
#
# a=count()
# print(a)
#
# f=lambda x,y:x*x+y*y
# print(f(2,3))

# def log(func):
# 	def inner(*args,**kwargs):
# 		print("helo")
# 		return func(*args,**kwargs)
# 	return inner
# @log
# def now():
# 	print("4141214")
#
# print(now())
# import functools
# #
# def log(text):
# 	def decorator(func):
# 		@functools.wraps(func)
# 		def wrapper(*args, **kw):
# 			print('%s %s():' % (text, func.__name__))
# 			func(*args, **kw)
# 			print('%s end %s():' % (text, func.__name__))
# 			return func
# 		return wrapper
# 	return decorator
#
#
# @log("haha")
# def now():
#     print('2015-3-25')
#
# now()

import functools
# int2=functools.partial(int,base=2)
# print(int2('1001'))
#
# kw = { 'base': 2 }
# print(int('10010', **kw))
#
# max2 = functools.partial(max, 10)
# print(max2(6,5,7))





