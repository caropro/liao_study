#coding=utf-8
# f=open("/Users/jianxuan/.nuke/NodePresets/user_presets.py",'r')
# for a in f:
# 	print(a)
# 	print(type(a))
# c=f.read()
# print(c)
#
# with open("/Users/jianxuan/.nuke/NodePresets/user_presets.py",'r') as f:
# 	print(f.read())
#
# for line in f.readlines():
# 	print(line.strip())




a=r"{'a':'b'}"
print(a)
print(type(a))
a=a.replace("{","")
a=a.replace("}","")
b=a.split(":")
print(b)


# b[0]=b[0][1:-1]
# b[1]=b[1][1:-1]
# print(b)
