#coding=utf-8
# import pickle
# f=open('test.txt','wb')
# b=dict(a=1,b=2,c="sb")
# pickle.dumps(b,f)


import json

class student(object):
	def __init__(self,name,age,score):
		self.name=name
		self.age=age
		self.score=score

def studenttt(std):
	return{
		"name":std.name,
		"age":std.age,
		"score":std.score
	}
b=student("Billy",34,69)

print(json.dumps(b,default=studenttt))

print(json.dumps(b,default=lambda obj:obj.__dict__))