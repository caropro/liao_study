#coding=utf-8
import re
a=r"D:/dsb123/comp/element/sad1234/afeg324"
d=a.split("/")

for i in d:
	c=re.search(r'(\w+\d+)$', i)
	if c:
		first=(d.index(i))
		break
	else:
		first=len(d)
final=d[:first+1]
path=''
for i in final:
	if path:
		path=path+'/'+i+'/'
	else:
		path=i
print(path)

