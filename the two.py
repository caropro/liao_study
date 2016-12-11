# -*- coding: utf-8 -*-
namelist=['nutJone','eggAnny','appleBill']
print(namelist)
print(len(namelist))
for i in range(len(namelist)):
	if i<len(namelist):
		print(i)
		print(namelist[i])
		a=-(len(namelist)-i)
		print(a)
		print(namelist[a])
		i+=1
#正数从零开始，倒数从-1开始算

namelist.append("peaTomas")
print(namelist)
#添加元素

namelist.insert(1,"xrayKael")
print(namelist)
#插入到指定位置

namelist.pop(2)
a=namelist.pop(2)
print(a)
print(namelist)
#删除指定位置元素，默认最后一个

namelist[1]="beefDanny"
print(namelist)
#按位置替换元素

list=[1,2,3]
listb=["a","b",list]
print(listb,"\n",listb[2][1])
#嵌套的list

l=[]
print(len(l))
#空列长度为0

t=(1,2,3)
print(t)
#元组数据

t=()
print(t)
#空元组

t=(1)
print(t)
t=(1,)
print(t)
#只有一个元素的元组，为消除歧义用逗号隔开

t=(1,2,["a","b"])
print(t,"\n",t[2][1])
print(t[2])
t[2][1],t[2][0]=t[2][0],t[2][1]
print(t[2])
#元组不可更改，但作为元素的列表中的元素却可以

#练习
L = [
    ['Apple', 'Google', 'Microsoft'],
    ['Java', 'Python', 'Ruby', 'PHP'],
    ['Adam', 'Bart', 'Lisa']
]
# 打印Apple:
print(L[0][0])
# 打印Python:
print(L[1][1])
# 打印Lisa:
print(L[-1][-1])



