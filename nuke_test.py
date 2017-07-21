#coding=utf-8
def jud(b):
	try:
		b=int(b)
	except:
		b=b
	return b
c=jud('123ss')
print(c,type(c))

a=["asdads",12313,"asd","a","12414"]
for i in a:
	p=jud(i)
	print(p,type(p))

a="'mov.mov32_fps': '30', 'mov.mov64_bitrate': '20000', 'checkHashOnRead': 'false', 'mov.mov32_codec': 'ap4h', 'file_type': 'mov', 'mov.mov64_fps': '30', 'colorspace': 'SLog', 'mov.mov64_codec': 'ap4h', 'raw': 'true', 'mov.meta_codec': 'ap4h', 'selected': 'true', 'file': 'hello world'"
print(a)
b=a.split(",")
d=reversed(b)
c=[x for x in d]
print(c)
for e in c:
	f=e.split(":")
	print(f)
	g=f[0][2:-1]
	h=f[1][2:-1]
	print(jud(h))
	k=jud(h)
	print(k,type(k))

