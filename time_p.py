#coding=utf-8
from datetime import  datetime
now=datetime.now()
print(now)
now=now.timestamp()
print(now)

n=datetime(2012,2,23,4,23,1)
print(n)
n=n.timestamp()
print(n)

s=1212412412.0
print(datetime.fromtimestamp(s))
print(datetime.utcfromtimestamp(s))