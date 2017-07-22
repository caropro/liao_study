#coding=utf-8
l=[x for x in range(10)]
print(l)
#内置循环的方式产生列表

l=[x*x for x in range(10)]
print(l)

l=[x*y for x in range(10) for y in "abcdefg"]
print(l)
#也可以多个变量循环

d={'a':1,'b':2,'c':3}
print(d.items())
print([(x,y) for x,y in d.items()])
#也可以读取dict中的对应元素

l=["Hello","World","hello","C++"]
print([s.lower() for s in l])
print([s.upper() for s in l])
print([s.capitalize() for s in l])
#字符串中的大写小写，首字母大写

#请修改列表生成式，通过添加if语句保证列表生成式能正确地执行：

# -*- coding: utf-8 -*-

L1 = ['Hello', 'World', 18, 'Apple', None]
print([i.lower() for i in L1 if isinstance(i,str)])

L2=[]
for i in L1:
	if isinstance(i,(int, float)) or i is None:
		pass
	else:
		print(i.lower())
		L2.append(i.lower())
print(L2)