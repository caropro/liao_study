#coding=utf-8
def sums(x):
	s=0
	for x in range(x+1):
		s+=x
	return s
print(sums(10))
print(sums(10000))
#之前的循环


def sums(x):
	if x==1:
		s=1
		return s
	elif x>1:
		return x+sums(x-1)
print(sums(10))
#这里就是sum（n）=sum（n-1）+n的理念，直到n=1的时候，因为继续下去是无限迭代所以要设置初始值来做停止

def suma(x):
	return sumb(x,1)
#定义函数时套上初始值，带到下一个函数去循环
def sumb(n,s):
	if n==1:
		return s
	return sumb(n-1,s+n)
print(suma(10))
#相当于从n一直加到1的逆推

# 练习
#
# 汉诺塔的移动可以用递归函数非常简单地实现。
#
# 请编写move(n, a, b, c)函数，它接收参数n，表示3个柱子A、B、C中第1个柱子A的盘子数量，然后打印出把所有盘子从A借助B移动到C的方法，例如：

def move(n, a, b, c):
	if n==1:
		print(a,' --> ',c)
	else:
		move(n-1,a,c,b)
#把n-1个放到b上
		move(1,a,b,c)
#把最大的直接放到c
		move(n-1,b,a,c)
#把n-1个放到c上
move(3, 'A', 'B', 'C')
#输出的时候是n==1时按照这里思路，先把a上的挪到b，c上，bc间互挪，再把b或者c上的挪回a
# 当A塔上有n个盘子是，先将A塔上编号1至n-1的盘子（共n-1个）移动到B塔上（借助C塔），然后将A塔上最大的n号盘子移动到C塔上，最后将B塔上的n-1个盘子借助A塔移动到C塔上。

#递归可以理解为找出一个线头，然后绕线，线头就是初始值。