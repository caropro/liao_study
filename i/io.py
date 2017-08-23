#coding=utf-8
# from io import StringIO
# f=StringIO()
# f.write("hello")
# f.write(" ")
# f.write("world")
# print(f.getvalue())

# from io import  StringIO
# f=StringIO("hello!\nHi\nGoodbye!")
# while True:
# 	s = f.readline()
# 	if s=='':
# 		break
# 	print(s.strip())


# from io import BytesIO
# f=BytesIO()
# f.write('中文'.encode('utf-8'))
#
# print(f.getvalue())

# f=BytesIO(b'\xe4\xb8\xad\xe6\x96\x87')
# print(f.read())
# import os
# os.name

import os
pt='/Users/jianxuan/Desktop/liao_study/'
# def one(s,k):
# 	for a_f in os.listdir(s):
# 		if os.path.isfile(os.path.join(s,a_f)):
# 			if k in os.path.splitext(a_f)[0]:
# 				print(s,a_f)
# 			if os.path.isdir(os.path.join(s,a_f)):
# 				one(os.path.join(s,a_f),k)
# one(pt,"fp")

import os
def search(dir, text):
    for x in os.listdir(dir):
        if os.path.isfile(os.path.join(dir,x)):
            if text in os.path.splitext(x)[0]:
                print('%s, %s'% (dir, x))
        if os.path.isdir(os.path.join(dir,x)):
            search(os.path.join(dir, x),text)


search(pt,'fp')