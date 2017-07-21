#coding=utf-8
def is_odd(n):
    return n % 2 == 1

a=list(filter(is_odd, [1, 2, 4, 5, 6, 9, 10, 15]))
print(a)
print(help(filter))

# filter(function or None, iterable) --> filter object
#  |
#  |  Return an iterator yielding those items of iterable for which function(item)
#  |  is true. If function is None, return the items that are true.
#判断返回值判断是不是真。

def not_empty(s):
    return s and s.strip()

list(filter(not_empty, ['A', '', 'B', None, 'C', '  ']))

s=[' ','','s']
for i in s:
	s=bool(i.strip())
	print(s)
#可以看出strip针对的数据
#
def _odd_iter():
	n = 1
	while True:
		n = n + 2
		yield n

def _not_divisible(n):
	return lambda x: x % n > 0

def primes():
	yield 2
	it = _odd_iter() # 初始序列
	while True:
		n = next(it) # 返回序列的第一个数
		yield n
		it = filter(_not_divisible(n), it) # 构造新序列
		print(it)

# 打印1000以内的素数:
for n in primes():
	if n < 1000:
		print(n)
	else:
		break

def test(n):
	yield lambda x: x % n > 0
a=test(3)
print(next(a))

print(lambda x:x!=2)


# 练习
#
# 回数是指从左向右读和从右向左读都是一样的数，例如12321，909。请利用filter()滤掉非回数：
# -*- coding: utf-8 -*-


def is_palindrome(n):
	return str(n) == str(n)[::-1]

	# 测试:
# print(is_palindrome(1212))
output = filter(is_palindrome, range(1,1000))
print(list(output))
#过滤时的返回值一定要是bool值才可以用，这里把数字转换成字符，正向等于反向即可达成