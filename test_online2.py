#coding=utf-8
class Palindrome:
	@staticmethod
	def is_palindrome(word):
		c=list(word.lower())
		b=c.copy()
		b.reverse()
		print(c)
		print(b)
		if c==b:
			return True
		else:
			return False
print(Palindrome.is_palindrome('Deleveled'))