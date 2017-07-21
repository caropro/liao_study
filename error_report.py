#coding=utf-8
# try:
# 	print("try.....")
# 	r=10/0
# 	print('result:',r)
# except ZeroDivisionError as e:
# 	print("except:",e)
# finally:
# 	print("finally...")
# print("End")


# def foo(s):
# 	return s/0
# def mu(s):
# 	return pow(foo(s),2)
# def main(s):
# 	try:
# 		mu(s)
# 	except Exception as e:
# 		print("except :" , e)
# 	finally:
# 		print("end")
# main(3)

# import logging
#
# def foo(s):
# 	return 10/int(s)
# def bar(s):
# 	return foo(s)**2
# def main():
# 	try:
# 		bar("0")
# 	except Exception as e:
# 		logging.exception(e)
# main()
#
# class errorC(ValueError):
# 	pass
#
# def foo(s):
# 	n=int(s)
# 	if n==0:
# 		raise errorC('valueError :',n )
# 	return 10/n
#
# foo(0)

# def foo(s):
# 	n=int(s)
# 	if n==0:
# 		raise ValueError('foo Error !')
# 	return 10/n
#
# def bar():
# 	try:
# 		foo('0')
# 	except Exception as e:
# 		print("bar",e)
# 		raise
# bar()



# def intinput(s):
# 	a=int(s)
# 	try:
# 		print(a/0)
# 	except Exception as e:
# 		print(e)
#
# intinput(10)

# try:
#     10 / 0
# except ZeroDivisionError:
#     raise ValueError('input error!')
#
# def foo(s):
#     n = int(s)
#     assert n != 0, 'n is zero!'
#     return 10 / n
#
# def main():
#     foo('0')
#
# main()
# n=100
# assert n>0,'n<0!!!'
# n=-10
# assert n>0,'n<0!!!'

# import logging
# logging.basicConfig(level=logging.INFO)
# s='0'
# n=int(s)
# logging.info('n=%d'% n)
# print(10/n)

# err.py
# import pdb
# s = '0'
# n = int(s)
# pdb.set_trace()
# print(10 / n)








