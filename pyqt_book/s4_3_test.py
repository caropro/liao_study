#coding=utf-8
import urllib
from urllib.request import urlopen

fh = urllib.request.urlopen("http://www.bankofcanada.ca/valet/observations/group/FX_RATES_DAILY/csv")
name=[]
ratedic={}
finalrate=[]
rate={}
date=''
for line in fh:
	l=str(line).strip()[2:-4]
	if l.startswith("FX"):
		l=l.split(",")
		name.append(l[0])
		ratedic[l[0]]=l[1]+l[2]
	elif l.startswith("ERROR"):
		break
	elif l.startswith("2017"):
		finalrate.append(l)

finalrate=finalrate[-1].split(",")
date=finalrate.pop(0)
for r,n in zip(finalrate,name):
	rate[n]=r
print(rate)
print(date)
print(finalrate)
print(name)
print(ratedic)