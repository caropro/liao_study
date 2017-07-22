#coding=utf-8
print(abs)
#内置函数之一的绝对值

a=abs
b=a(-11)
print(a,b)
#abs="aaa"
#print(abs)
#可以将变量指向函数，函数名（指向函数的变量）也可以指向变量

def ak(a,b,c):
	print(c(a),c(b))
a=10
b=-10
c=abs
ak(a,b,c)
#函数中变量可以嵌套函数----高阶函数
#（把函数作为参数传入，这样的函数称为高阶函数，函数式编程就是指这种高度抽象的编程范式。）



